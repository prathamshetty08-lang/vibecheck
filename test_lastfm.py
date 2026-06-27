import requests

API_KEY = "2441261acaa9251de4a1e8c9df5949c5"

url = "https://ws.audioscrobbler.com/2.0/"

params = {
    "method": "tag.gettoptracks",
    "tag": "happy",
    "api_key": API_KEY,
    "format": "json"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.text[:500])