import requests

def upload_image(url, path):
    data = {'Upload': 'Upload', 'MAX_FILE_SIZE': 100000000}
    files = {'uploaded': (path, open(path, 'rb'), "image/jpeg")}
    request = requests.post(url, files=files, data=data)
    for line in request.text.splitlines():
        if 'flag' in line:
            print(line)


upload_image("http://10.11.249.222/?page=upload", "/Users/nesta/Desktop/42/darkly/README.md")
