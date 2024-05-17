import os
import threading


def print_numbers():
    thread_name = threading.current_thread().name
    for i in range(1, 6):
        print(f"Number: {i} - Thread: {thread_name} - ProcessID: {os.getpid()} ")


def print_letters():
    thread_name = threading.current_thread().name
    for letter in 'abcde':
        print(f"Letter: {letter} - Thread: {thread_name} - ProcessID: {os.getpid()} ")


def thread_function():
    # Create threads
    number_thread = threading.Thread(target=print_numbers, name="NumberThread")
    letter_thread = threading.Thread(target=print_letters, name="LetterThread")

    # Start threads
    number_thread.start()
    letter_thread.start()

    # Wait for threads to complete
    number_thread.join()
    letter_thread.join()


def main():
    """Main thread function starting."""
    print("Running main thread function...\n")
    thread_function()
    print(f"Threads executed.")


if __name__ == "__main__":
    main()
