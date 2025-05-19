import requests

REGISTRY_URL = "http://localhost:8443/serviceregistry/register"

payload = {
    "serviceDefinition": "room-temperature-sensor",
    "providerSystem": {
        "systemName": "room-temp-sensor-1",
        "address": "localhost",
        "port": 8081
    },
    "serviceUri": "/",
    "secure": "NOT_SECURE",
    "interfaces": [
        "HTTP-INSECURE-JSON"
    ],
    "metadata": {
        "unit": "celsius"
    }
}

response = requests.post(REGISTRY_URL, json=payload)
print("[✅] Publisher registration:", response.status_code, response.text)
