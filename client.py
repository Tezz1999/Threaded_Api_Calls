import requests
import json

points = [[41.3432,-72.8816],[41.8011,-72.8608],[41.567,-73.5122]]
#new haven, hfd, newburgh
for lat,lon in points:
    url = f'http://localhost:5000/getByPoint?point={lat},{lon}'
    r = requests.get(url)
    data = json.loads(r.text)
    print(lat,lon)
    for res in data['results']:
        print("\t",res['hex'],res['date_time'],res['lat'],res['lon'],res['dist'])