import base64
from openai import OpenAI

endpoint = "https://gradeatron6969-resource.services.ai.azure.com/openai/v1"
api_key = "6vhla59vTfjsMm55f6a1CpzA9Ytz59jt8lW3e0I07OkFq4zvw3jdJQQJ99CFACfhMk5XJ3w3AAAAACOGcpOH"
deployment_name = "gpt-4.1-mini"

client = OpenAI(base_url=endpoint, api_key=api_key)

# Read and encode the PDF
with open("/home/ebsen/Desktop/MintDrive/Skrivebord/uni/AI stat eval/MLFall2025.pdf", "rb") as f:
    pdf_data = base64.b64encode(f.read()).decode("utf-8")

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in the pdf?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:application/pdf;base64,{pdf_data}"
                    }
                }
            ]
        }
    ],
)

print(completion.choices[0].message.content)