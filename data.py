import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

quiz_data = requests.get(url="https://opentdb.com/api.php", params=parameters)
quiz_data.raise_for_status()
question_data = quiz_data.json()["results"]
