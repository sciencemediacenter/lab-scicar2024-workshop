# Strukturierte Daten aus Bildern extrahieren

## Flow

## Programmatischer Aufruf

```python
import requests
API_URL = "http://localhost:3000/api/v1/prediction/&#x3C;chatlfowid>"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Can you describe the image?",
    "uploads": [
        {
            "data": 'data:image/png;base64,iVBORw0KGgdM2uN0', # base64 string or url
            "type": 'file', # file | url
            "name": 'Flowise.png',
            "mime": 'image/png'
        }
    ]
})
```

```bash

image="

curl http://localhost:3333/api/v1/prediction/16b1492d-08e8-4484-8590-551a786e1045 \
     -X POST \
     -d '{"question": "Do", "uploads": [
        {
            "data":"data:image/png;base64, @$image",
            "type":"file",
            "name":"ticket.png",
            "mime": "image/png"
        }
        ]}' \
     -H "Content-Type: application/json"

```