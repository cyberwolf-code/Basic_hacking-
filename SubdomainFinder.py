import requests

def find_subdomains(domain, wordlist):
    print(f"\n[+] Finding subdomains for: {domain}\n")
    for sub in wordlist:
        url = f"http://{sub}.{domain}"
        try:
            res = requests.get(url, timeout=3)
            print(f"[+] Found: {url} ({res.status_code})")
        except requests.exceptions.RequestException:
            pass  # Ignore failed requests

if __name__ == "__main__":
    target_domain = input("Enter domain (e.g., example.com): ").strip()
    subdomains = ["www", "mail", "blog", "shop", "dev", "api", "test", "vpn", "cpanel", "admin"]
    find_subdomains(target_domain, subdomains)
