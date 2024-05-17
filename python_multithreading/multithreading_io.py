import os
import threading
import time


def read_file_simulated(file_name):
    print(f"Reading {file_name}")
    print(f"Task assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running read task: {os.getpid()}")
    time.sleep(2)  # Simulate a time-consuming read operation
    print(f"Finished reading {file_name}")


def read_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', file_name)
    relative_path = os.path.relpath(file_path, start=os.getcwd())  # The relative path from current directory
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        # Get the current thread object and its name
        thread_name = threading.current_thread().name
        print(f"Read from {relative_path}: {first_line} - Thread: {thread_name} - ProcessID: {os.getpid()}")


def thread_function():
    # Files to read
    files = ['file1.txt', 'file2.txt', 'file3.txt']

    # Creating and starting threads for each file
    threads = []
    for file in files:
        thread = threading.Thread(target=read_file, args=(file,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


def main():
    """Main thread function starting."""
    print("Running main thread I/O function...")
    thread_function()
    print(f"Threads executed.")


if __name__ == "__main__":
    main()
