# Function Hijacking AND Cross Site Scripting (XSS)

## Description

This occurs when you replace or define a JavaScript function that the application expects to exist. By overriding the function and setting its behavior (e.g., returning `true`), you bypass the intended logic or validation in the front-end. Insecure reliance on client-side JavaScript functions for critical operations makes this type of attack possible.

When you injected the `<script>` tag, you executed arbitrary JavaScript code in the context of the application. This is a classic example of XSS, specifically Stored XSS or Reflected XSS, depending on whether your input was stored on the server or immediately reflected back in the response.

## BornToSec
At the moment I write this readme, there is a mistake. I think the aim of this page is to learn more about function hijacking and XSS but you dont need any of this to get the flag. You can simply write `script` in the message field and the flag will be displayed.

Even if you don't need to use function hijacking or XSS to get the flag, I will still explain how you could do it.
When you click on the button without any message or name, you will see an alert that tells you that you cant send empty fields. You also have a error on your console that inform you that the function `checkForm` is not defined.

You can now define the function checkForm in the console and just tell the function to return true when the form is submitted. You can do this by typing the following in the console: 
```javascript
function checkForm() {
	document.querySelector('[name=guestform]').setAttribute('onsubmit', 'return true;');
}
```

Now you can submit the form without any message or name.

For the xss part, you can inject the following code in the message field:
```html
<script>alert('XSS')</script>
```
If the input is not well sanitized, you should get an alert with the message 'XSS'.

## How to prevent it
- Validate Input on Both Client and Server: Ensure all user inputs are sanitized and validated before processing and reject potentially harmful characters like `<`, `>`, and `script` tags.
- Use Content Security Policy (CSP): Implement CSP headers to restrict the execution of unauthorized scripts.
- Avoid Relying on Client-Side Validation for Security: Perform critical checks on the server side instead of relying solely on JavaScript.
- Secure JavaScript Functions: Avoid exposing sensitive logic in client-side code.