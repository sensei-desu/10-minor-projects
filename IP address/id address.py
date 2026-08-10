import urllib.request
import json

def get_public_ip():
    print("=== Public IP Address Finder ===")
    try:
        url = "https://api.ipify.org?format=json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        print(f"\nYour Public IP Address: {data['ip']}")
    except Exception as e:
        print(f"\nCould not retrieve IP: {e}")
        
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    get_public_ip()
