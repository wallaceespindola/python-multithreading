import concurrent.futures
import os
import threading as th

# A global variable and a lock to control access to this variable
counter = 0
lock = th.Lock()


def worker():
    global counter
    with lock:  # Ensure thread-safe modification of the shared counter
        print(f"Counter thread running - Thread: {th.current_thread().name} - ProcessID: {os.getpid()} ")
        for _ in range(1000000):  # Simulate some work
            counter += 1


def run_workers():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(worker) for _ in range(2)]
        # Wait for all futures to complete
        concurrent.futures.wait(futures)
    print(f"Main thread continuing to run - Thread: {th.current_thread().name} - ProcessID: {os.getpid()} ")
    return counter


if __name__ == "__main__":
    run_workers()
    print(f"Final counter value: {counter} - Thread: {th.current_thread().name} - ProcessID: {os.getpid()} ")
