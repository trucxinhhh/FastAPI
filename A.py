import requests

url = 'http://127.0.0.1:8000/submit'
files = [('files', open('test_files/a.txt', 'rb')), ('files', open('test_files/b.txt', 'rb'))]
payload ={"name": "foo", "point": 0.13, "is_accepted": False}
resp = requests.post(url=url, data=payload, files=files) 
print(resp.json())