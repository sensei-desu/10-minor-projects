import urllib.request
import json
import urllib.error

def fetch_github_user():
    print("=== GitHub User Inspector ===")
    
    while True:
        username = input("\nEnter a GitHub username (or 'q' to quit): ").strip()
        
        if username.lower() == 'q':
            print("Bye!")
            break

        if not username:
            continue

        url = f"https://api.github.com/users/{username}"
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))

            print(f"\n--- GitHub Info for {data.get('login')} ---")
            print(f"Name        : {data.get('name', 'N/A')}")
            print(f"Public Repos: {data.get('public_repos', 0)}")
            print(f"Followers   : {data.get('followers', 0)}")
            print(f"Bio         : {data.get('bio') or 'No bio provided.'}")

        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(" User not found!")
            elif e.code == 403:
                print(" GitHub API rate limit exceeded. Try again later.")
            else:
                print(f" HTTP Error: {e.code}")
        except Exception as e:
            print(f" Connection error: {e}")

if __name__ == "__main__":
    try:
        fetch_github_user()
    except Exception as e:
        print(f"\n Script crashed: {e}")
    finally:
        input("\nPress Enter to exit...")