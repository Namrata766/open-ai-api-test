import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://nam766embeddings.openai.azure.com/",
    api_version="2023-03-15-preview",
    api_key=os.environ['AZURE_OPENAI_KEY']
)

response = client.embeddings.create(
    model="testembedding",
    input="cat"
)

# print(response)
print(response.data[0].embedding)
