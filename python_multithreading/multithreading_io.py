import os
import threading
import time


def read_file_simulated(file_name):
    print(f"Reading {file_name}")
    time.sleep(2)  # Simulate a time-consuming read operation
    print(f"Finished reading {file_name}")


def read_file(file_name):
    base_path = os.path.dirname(__file__)  # gets the directory in which the script resides
    file_path = os.path.join(base_path, '..', 'resources', file_name)
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        # Get the current thread object and its name
        thread_name = threading.current_thread().name
        print(f"{thread_name} read from {file_path}: {first_line}")


def thread_function():
    # Files to read
    files = ['../resources/file1.txt', '../resources/file2.txt', '../resources/file3.txt']

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
