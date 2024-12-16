# Hidden Field Manipulation

## Description
Hidden Field Manipulation is an attack that can be used to change the value of a hidden field in a form. This attack is typically used to change the price of an item being purchased in an online store.

## BornToSec
In our case, I went to the page recover. In this page there is only a text and a submit button. Then I inspect the page and I discover a hidden input.

```html
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

Then I change the value of the hidden input and I submit the form. The flag is displayed.