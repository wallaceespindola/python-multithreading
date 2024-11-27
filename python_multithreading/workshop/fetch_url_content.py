from concurrent.futures import ThreadPoolExecutor

import requests


def fetch(url):
    response = requests.get(url)
    result = f"\nURL: {url} \nCONTENT: \n{response.text}"
    print(result)
    return result


def main():
    urls = ["https://www.linkedin.com/learning/certificates/c0a8d780542b8e06ea4127e1066521a650f9e40bf856b05a9417238dd83131c6",
            "https://www.16personalities.com/profiles/df7ab52cddc34",
        "https://example.com", "https://example.org", "https://example.net"]

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch, urls))
        print(f"ALL RESULTS: \n{results}")

    print("Fetched the content of all URLs!")


if __name__ == "__main__":
    main()
