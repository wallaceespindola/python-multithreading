import os
import threading


def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def main():
    """Main function for demonstration purposes."""
    print("Running main function...")
    x = 10
    y = 5
    result = add(x, y)
    print(f"Task assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task: {os.getpid()}")
    print(f"The sum of {x} and {y} is {result}")


if __name__ == "__main__":
    main()
