import json
import requests
import os
import numpy as np
with open("data1.json", "r") as f:
    data = json.load(f)

responce_list = []
batch_number = int(os.path.splitext(os.path.basename(__file__))[0][5:])
batches = np.array_split(data, 10)

for datapoint in batches[batch_number-1][400:]:
    response = requests.post("http://127.0.0.1:11434/v1/chat/completions", json={
    "model": "gpt oss",
    "messages": [{"role": "user", "content": f"""
            These are my answers to the multiple choice questions where, 0 is the first answer choice, 1 is the second answer choice:{datapoint}
            Heres the test:
            What's Bigger?
            1. Earth or Mars
            2. Africa or South America
            3. The Old Testament or the New Testament, by length
            4. The heaviest human ever or the heaviest pumpkin ever
            5. The annual budget of the French government or the annual revenue of Google
            6. The number of people on Earth or the number of trees
            7. An atom of Nitrogen or an atom of Uranium
            8. The tallest building or the tallest tree
            9. A gigabyte or a terabyte
            10. The population of Arizona or the population of Estonia
            11. Buckingham Palace or the White House, by number of bedrooms
            12. A violin or a viola
            13. A chromosome or a gene
            14. Your pancreas or your pituitary gland
            15. A division or a regiment
            """}],
    "stream": False
    })
    responce_list.append(response.json()["choices"][0]["message"]["content"])
    #Save to json file
    with open(f"responce{batch_number}{batch_number}{batch_number}.json", "w") as f:
        json.dump(responce_list, f)
print(responce_list)