import time
from gmaps import Geocoding

api = Geocoding()

PLACES = (
    'Vien','Zadar','Berlin'
)

def fetch_place(place):
    geocoded = apiu.geocoding(place)[0]

    print("{:25s},{:6.2f},{:6.2f}".format(
        geocoded['formatted_address'],
        geocoded['geometry']['location']['lat'],
        geocoded['geometry']['location']['lng']
    ))

def main():
    for place in PLACES:
        fetch_place(place)

if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print("time elapsed:{:.2f}s".format(elapsed))

