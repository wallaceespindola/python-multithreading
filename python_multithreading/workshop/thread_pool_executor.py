from concurrent.futures import ThreadPoolExecutor


def task(n):
    print(f"Processing {n}")


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(task, range(1, 4))

    print(results)


if __name__ == "__main__":
    main()
