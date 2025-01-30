import requests

params = {'prompt':input('Make your request, meatbag.\n')}

r = requests.get('http://192.168.1.7:5000', params=params)


print(str(r.content))
