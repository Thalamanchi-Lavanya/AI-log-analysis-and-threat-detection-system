import requests

response = requests.get(
    "https://api.github.com"
)

print("Status Code:", response.status_code)

data = response.json()

print("Current User URL:")
print(data["current_user_url"])