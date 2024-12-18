# Hard-Coded Credentials

## Description
Passwords are embedded directly in source code, configuration files, or firmware, making them accessible to anyone with access to the code or files.

## BornToSec
Because we got a ip here 10.11.249.222, we are able to do a nmap scan on it to see what services are running on it.

```bash
nmap -v -A 10.11.249.222
```

Here, we got a lot of information about the services running on the machine. But the most interesting is http-methods. 

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

We can see that the server is running nginx 1.4.6 (Ubuntu) and that it supports GET, HEAD and POST methods. We also have a robots.txt file with 2 disallowed entries. Let's check them out.

If you open the url `http://10.11.249.222/robots.txt`, you will see the following:

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

We can see that we have 2 disallowed entries, `/whatever` and `/.hidden`. Let's check them out.

If you open the url `http://10.11.249.222/whatever`, you will be able to download the file `htpasswd` which is usually used to store some hashed passwords.

Here is the content of the file:

```
root:437394baff5aa33daa618be47b75cb49
```

We can now decode this hash with md5 and we will get the password `qwerty123@`.

Now as i already know the password for root user in the signin page i know that these credentials are for another page so i will try to login with these credentials on the page `http://10.11.249.222/admin/`.

And here we go, we are able to login with the credentials `root:qwerty123@` and we are able to see the flag.

## How to prevent it
- Strong Hashing Algorithms: Use modern algorithms like bcrypt, Argon2, or PBKDF2 for password storage.
- Access Controls: Restrict access to sensitive files and directories (e.g., .htpasswd).
- Multi-Factor Authentication (MFA): Add an additional layer of security to reduce reliance on passwords alone.