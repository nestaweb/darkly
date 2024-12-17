# Cross-site Scripting (XSS)

## Description
Cross-site scripting (XSS) is a client-side code injection attack. The attacker aims to execute malicious scripts in a web browser of the victim by including malicious code in a legitimate web page or web application. Vulnerable vehicles that are commonly used for cross-site scripting attacks are forums, message boards, and web pages that allow comments.

## BornToSec
The only clickable image on the index is the nsa logo.
When you click on it, it redirects you to the `index.php?page=media&src=nsa` page.
Then if you look at the source code, you can see that the logo is not loaded in the img tag but in a object tag.
You can only observe that when you change the parameter src in the url to something else like `index.php?page=media&src=okok`, it will change the data of the obect tag to `okok`.
We now know that the parameter src is vulnerable to XSS.

To exploit this vulnerability, we can input data in the object tag with base64 encoding.
I went to a base64 encoder website and encoded the following script:

```html
<script>
alert('Hello World')
</script>
```

and then I changed the parameter src in the url to `index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnSGVsbG8gV29ybGQhJyk8L3NjcmlwdD4=`.
And it worked, I got the flag.

## How to prevent it
- Validate and Sanitize Input: Ensure all user inputs are validated on both client and server sides.
- Restrict Allowed Sources: Implement a Content Security Policy (CSP) to restrict what sources can be loaded in tags like `<object>`, `<iframe>`, or `<script>`.
- Avoid Dynamic Content Loading: Avoid using dynamic attributes like `data`, `src`, or `href` with untrusted user input.