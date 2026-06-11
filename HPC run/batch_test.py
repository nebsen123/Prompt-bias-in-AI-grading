import json
import requests
import os
import numpy as np
with open("data.json", "r") as f:
    data = json.load(f)

responce_list = []

for datapoint in data[:10]:
    response = requests.post("http://localhost:11434/v1/chat/completions", json={
        "model": "qwen3",
        "messages": [{"role": "user", "content": f"..."}],
        "stream": False
    })
    responce_list.append(response.json()["choices"][0]["message"]["content"])
print(responce_list)
#Save to json file
with open(f"responce_test.json", "w") as f:
    json.dump(responce_list, f)