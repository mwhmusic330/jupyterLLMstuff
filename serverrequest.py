import requests

params = {'prompt':input('Make your request, meatbag.\n')}

r = requests.get('http://192.168.1.28:5000/request', params=params)


print(str(r.content.decode('utf-8')))
