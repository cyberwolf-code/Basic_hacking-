import requests

def fetch_website(url):
    try:
        print(f"\n[+] Fetching: {url}")
        response = requests.get(url, timeout=5)

        print(f"\n[+] Status Code: {response.status_code}")
        print("\n[+] Headers:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")

        print("\n[+] Preview of Content:")
        print(response.text[:500])  # show first 500 characters

    except requests.exceptions.RequestException as e:
        print("\n[!] An error occurred:")
        print(f"  {e}")

if __name__ == "__main__":
    target = input("Enter the Target URL (e.g., https://example.com): ").strip()
    if not target.startswith("http"):
        target = "https://" + target
    fetch_website(target)

