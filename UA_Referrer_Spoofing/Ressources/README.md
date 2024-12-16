# User-Agent and Referrer Spoofing

## Description
This technique involves manipulating HTTP headers to trick the server into believing that the request is coming from a different source or client.

## BornToSec
When you click on the copyright icon, it redirects you to the following URL:
```
http://10.11.249.222/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
````

If you inspect the html, you will see some useless information. But if you look closer, you will see two key elements:
```html
<!--
	You must come from : "https://www.nsa.gov/".
-->
```
and
```html
<!--
	Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```

The referrer tells the web server where the request originated from, and the User-Agent header provides information about the client's browser. By setting these headers to the expected values, you can access the flag.

```bash
curl --referer "https://www.nsa.gov/" --user-agent "ft_bornToSec" http://10.11.249.222/\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

## How to prevent it
- Server-Side Validation: Do not rely solely on client-provided headers for security decisions. Implement server-side checks and validations.
- Use of Tokens: Instead of relying on headers for authentication or authorization, use secure tokens or session management.
- Logging and Monitoring: Track unusual patterns in User-Agent and Referrer headers to detect potential spoofing attempts.
