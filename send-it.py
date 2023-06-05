import json
import requests

webhook_url = ''

data = {
    "content": "**Message**",
    "embeds": [
        {
            "title": "Example",
            "description": "Gato Gato but Gato Gato **GATO**\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "color": None,
            "fields": [
                {
                    "name": "Gato Below: (Not Inline)",
                    "value": "Lorem ipsum"
                },
                {
                    "name": "hI MY NAME IS INLINE!!!",
                    "value": "Im an inline function!!! alltho i look dumb cause the idiot above me isnt inline so nothing really changed here",
                    "inline": True
                },
                {
                    "name": "Hey inline my name is InlineGato7",
                    "value": "And im here to fix that. Im inline now.\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    "inline": True
                }
            ],
            "author": {
                "name": "MatchPort's Disco Hook C# Json Data Sender"
            }
        }
    ],
    "attachments": []
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

if response.status_code != 204:
    raise ValueError(f'Request to discord returned an error {response.status_code}, the response is:\n{response.text}')
