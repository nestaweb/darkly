# Cookies Manipulation

## Description
Cookies Manipulation is an attack that can be used to change the value of a cookie in a web browser. This attack is typically used to gain unauthorized access to a system.

## BornToSec
First if you use Chrome, you can open your inspector and go the the Application tab. You will see the cookies of the website. You can see that there is a cookie named `I_am_admin` with the value '68934a3e9455fa72420237eb05902327'.

Then I went to a hash analyzer website and I discovered that the hash '68934a3e9455fa72420237eb05902327' is th hash of 'false' with the MD5 algorithm.

So I went to a MD5 hash generator and I generated the hash of 'true' which is 'b326b5062b2f0e69046810717534cb09'.

Then I changed the value of the cookie `I_am_admin` to 'b326b5062b2f0e69046810717534cb09' and I refreshed the page. The flag is displayed.

## How to prevent it
To prevent Cookies Manipulation, you should not store sensitive information in cookies. Instead, you should store sensitive information on the server side and only use cookies for non-sensitive information. You should also ensure that the cookies are encrypted and signed to prevent tampering.

MD5 is considered cryptographically weak due to its susceptibility to:
- Hash collisions: Two different inputs can produce the same hash.
- Fast computation: Makes brute-forcing or dictionary attacks feasible.
- Lack of integrity checks: It does not provide mechanisms to verify data authenticity.

Its better to use SHA-256 combined with a secret key.
