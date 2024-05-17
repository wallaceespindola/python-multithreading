import concurrent.futures
import os
import threading as th
import time


def worker():
    time.sleep(1)  # Simulate a time-consuming operation
    print(f"Worker thread running - Thread: {th.current_thread().name} - ProcessID: {os.getpid()} ")


def run_workers():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(worker)
        pool.submit(worker)
    print(f"Main thread continuing to run - Thread: {th.current_thread().name} - ProcessID: {os.getpid()} ")


if __name__ == "__main__":
    run_workers()
