import threading


def do_something():
    print("Look, I'm running in a thread!")


def main():
    # Create a thread
    thread = threading.Thread(target=do_something)

    # Start the thread
    thread.start()

    # Wait for the thread to complete
    thread.join()

    print("All done!")


if __name__ == "__main__":
    main()
