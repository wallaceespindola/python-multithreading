import threading


def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")


def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")


def thread_function():
    # Create threads
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for threads to complete
    thread1.join()
    thread2.join()


def main():
    """Main thread function starting."""
    print("Running main thread function...")
    thread_function()
    print(f"Threads executed.")


if __name__ == "__main__":
    main()
