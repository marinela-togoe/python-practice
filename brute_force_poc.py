import requests

url = "http://192.168.0.1/login.php"
data = {"username": "admin", "password": "admin"}
response = requests.post(url, data=data)

if "Welcome" in response.text:
    print("Login successful")
else:
    print("Login failed")
