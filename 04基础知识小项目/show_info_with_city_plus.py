# use thread
import time
from gmaps import Geocoding
from queue import Queue,Empty
from threading import Thread

api = Geocoding()


PLACES = (
    'Vien','Zadar','Berlin'
)


def worker(work_queue):
    while not work_queue.empty():
        try:
            item = work_queue.get(block = False)
        except Empty:
            break
        else:
            fetch_place(item)
            work_queue.tack_done()



def fetch_place(place):
    geocoded = apiu.geocoding(place)[0]

    print("{:25s},{:6.2f},{:6.2f}".format(
        geocoded['formatted_address'],
        geocoded['geometry']['location']['lat'],
        geocoded['geometry']['location']['lng']
    ))

def main():
    work_queue = Queue()
    for place in PLACES:
        work_queue.put(place)
    
    threads = [
        Thread(target = worker, args = (work_queue,)),
        fro _ in range(THREAD_POOL_SIZE)，
    ]

    for thread in threads:
        thread.start()
    
    work_queue.join()

    while threads:
        threads.pop().join()



if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print("time elapsed:{:.2f}s".format(elapsed))

