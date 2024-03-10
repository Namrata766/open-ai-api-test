import os
import numpy
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://nam766embeddings.openai.azure.com/",
    api_version="2023-03-15-preview",
    api_key=os.environ['AZURE_OPENAI_KEY']
)

response = client.embeddings.create(
    model="testembedding",
    input=['India has a great culture', 'Indian culture is rich']
)

# print(response)
embedding1 = response.data[0].embedding
embedding2 = response.data[1].embedding

similarity_score = numpy.dot(embedding1, embedding2)

print(similarity_score * 100, '%')