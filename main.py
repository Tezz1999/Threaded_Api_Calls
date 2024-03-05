import json,pymysql,time
from flask import Flask
from flask import request,redirect
import datetime

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])

def root():
    res={}
    res['code']=1
    res['msg']='No Endpoint specified'
    res['req']='/'
    return json.dumps(res,indent=4)


@app.route("/getByPoint",methods=['GET','POST'])
def getByPoint():
    res={}
    point=request.args.get("point")
    cords=point.split(",")
    try:
        lat=float(cords[0])
        long=float(cords[1])
    except Exception as e:
        print(e)
        res['code']=0
        res['msg']='Invalid lat/lon value (NaN)'
        return json.dumps(res,indent=4)
        
    
    if (round(abs(long)) not in range(1,180)):
        res['code']=0
        res['msg']='Invalid longitude value'
        return json.dumps(res,indent=4)
    elif (round(abs(lat)) not in range(1,90)):
        res['code']=0
        res['msg']='Invalid Latitude value'
        return json.dumps(res,indent=4)

    conn=pymysql.connect(host="", port=3306, user='',passwd='', db='', autocommit=True)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    
    sql='''SELECT *,st_distance_sphere(geo_point, 
    ST_GeomFromText('POINT(%s %s)',4326)) as dist 
    FROM `conlontj_datapoints`  order by dist LIMIT 0,2;
        '''

    start_time=time.time()
    cur.execute(sql,(long, lat))
    end_time=time.time()
    res['code']=1
    res['msg']='ok'
    output=[]
    for row in cur:
        item={}
        item=row
        del item['geo_point']
        item['date_time'] = str(row['date_time'])
        if item['lat'] is not None:
            item['lat'] = float(item['lat'])
        if item['lon'] is not None:
            item['lon'] = float(item['lon'])
        if item['gs'] is not None:
            item['gs'] = float(item['gs'])
        if item['track'] is not None:
            item['track'] = float(item['track'])
        if item['nav_heading'] is not None:
            item['nav_heading'] = float(item['nav_heading'])
        output.append(item)
    res['results']=output
    res['num_results']=len(output)
    res['sql_time']=round(end_time-start_time,2)
    res['req']='/getByPoint'
    return json.dumps(res,indent=4)


if __name__=='__main__':
    app.run(host='127.0.0.1',debug=True)