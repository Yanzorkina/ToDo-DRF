import requests

response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':'user2', 'password': 'r5yrq9s4'})
print(response.status_code)
print(response.json())