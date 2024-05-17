import threading
from threading import Lock

lock = Lock()
shared_resource = []


def safely_add(item):
    with lock:
        shared_resource.append(item)


def main():
    threads = [threading.Thread(target=safely_add, args=(i,)) for i in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(shared_resource)


if __name__ == "__main__":
    main()
