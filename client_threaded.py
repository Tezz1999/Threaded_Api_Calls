
import requests
import json
import threading

# Function to make a request to the API
def make_request(lat, lon):
    url = f'http://localhost:5000/getByPoint?point={lat},{lon}'
    r = requests.get(url)
    data = json.loads(r.text)
    with threading.Lock(): # Ensuring thread-safe printing
        print(lat, lon)
        for res in data['results']:
            print("\t", res['hex'], res['date_time'], res['lat'], res['lon'], res['dist'])

def main():
    points = [[41.3432, -72.8816], [41.8011, -72.8608], [41.567, -73.5122]] 
    threads = []
    for lat, lon in points:
        thread = threading.Thread(target=make_request, args=(lat, lon))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join() # Ensuring all threads complete before the script ends

if __name__ == '__main__':
    main()
