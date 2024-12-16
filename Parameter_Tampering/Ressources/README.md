# Paramter Tampering

## Description
Parameter Tampering is an attack that can be used to change the value of a parameter in a URL. This attack is can be used to retrieve sensitive information or to gain unauthorized access to a system.

## BornToSec
When you click on any social media icon on the site, it first redirects to an internal page with the following URL:

```http
http://10.11.249.222/index.php?page=redirect&site=instagram
```

You can see it by inspecting the footer.

Than if you change to the following URL:

```http
http://10.11.249.222/index.php?page=redirect&site=someotherwebsite
```

You will be redirected to the page with the flag.

## How to prevent it
To prevent Parameter Tampering, you should validate the parameters in the URL to ensure that they are not being tampered with. You should also avoid passing sensitive information in the URL whenever possible.