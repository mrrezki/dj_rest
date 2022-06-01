import requests

headers = {"Authorization": "Bearer 8e71066cb6b72a5509ce36c9a0912c8e0cdab4b7"}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done",
    "price": 29.76,
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
