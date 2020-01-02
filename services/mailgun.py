import json

import requests

DOMAIN = '<mailgun domain>'
API_KEY = '<maingun apikey>'

# DOMAIN = 'sandbox4fb41143314241f9ad86cbc75b82f387.mailgun.org'
# API_KEY = 'd9df603df7624ffec7178b45b92632f3-1df6ec32-a08c93f6'


def send_email(email, subject, content):
    response = requests.post(
        "https://api.mailgun.net/v3/"+DOMAIN+"/messages",
        auth=("api", API_KEY),
        data={"from": "Mailgun Sandbox <postmaster@"+DOMAIN+">",
              "to": email,
              "subject": subject,
              "text": content})

    json_response = json.loads(response.text)

    return json_response


def check_email_status(message_id):
    response = requests.get(
        "https://api.mailgun.net/v3/"+DOMAIN+"/events",
        auth=("api", API_KEY),
        params={"message-id": message_id,
                })

    json_response = json.loads(response.text)

    return json_response
