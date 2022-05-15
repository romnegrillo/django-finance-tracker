from urllib import response
import requests

endpoint = "http://localhost:8000/finance/income/"
json_data = {
    "wallet": 3,
    "category": "Investment",
    "total": 100000,
    "description": "Withdraw investment.",
    "date": "2022-05-14"
}

response = requests.post(endpoint, json=json_data)
print(response.json())