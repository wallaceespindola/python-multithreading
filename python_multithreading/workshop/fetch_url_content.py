from concurrent.futures import ThreadPoolExecutor

import requests


def fetch(url):
    response = requests.get(url)
    result = f"\nURL: {url} \nCONTENT: \n{response.text}"
    print(result)
    return result


def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch, urls))
        print(f"ALL RESULTS: \n{results}")

    print("Fetched the content of all URLs!")


if __name__ == "__main__":
    main()
