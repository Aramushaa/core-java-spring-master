import requests

REGISTRY_URL = "http://localhost:8443/serviceregistry/register"

payload = {
    "serviceDefinition": "room-temp-subscriber",
    "providerSystem": {
        "systemName": "subscriber-1",
        "address": "localhost",
        "port": 8083
    },
    "serviceUri": "/",
    "secure": "NOT_SECURE",
    "interfaces": [
        "HTTP-INSECURE-JSON"
    ],
    "metadata": {
        "role": "logger"
    }
}

response = requests.post(REGISTRY_URL, json=payload)
print("[✅] Subscriber 1 registration:", response.status_code, response.text)
