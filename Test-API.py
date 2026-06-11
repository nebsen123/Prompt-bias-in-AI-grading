import base64
from openai import OpenAI
import pymupdfy

endpoint = "https://gradeatron6969-resource.services.ai.azure.com/openai/v1"
api_key = "6vhla59vTfjsMm55f6a1CpzA9Ytz59jt8lW3e0I07OkFq4zvw3jdJQQJ99CFACfhMk5XJ3w3AAAAACOGcpOH"
deployment_name = "gpt-4.1-mini"

client = OpenAI(base_url=endpoint, api_key=api_key)

# Extract text from PDF
pdf_path = "/home/ebsen/Desktop/MintDrive/Skrivebord/uni/AI stat eval/MLFall2025.pdf"
doc = pymupdf.open(pdf_path)
pdf_text = "\n\n".join(page.get_text() for page in doc)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": f"What is in this document?\n\n{pdf_text}"
        }
    ],
)
print(completion.choices[0].message.content)