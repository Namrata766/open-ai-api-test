# Note: The openai-python library support for Azure OpenAI is in preview.
# Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://nam766practiceai.openai.azure.com/",
    api_version="2024-02-15-preview",
    api_key=os.environ['AZURE_OPENAI_KEY']
)

message_text = [{"role": "system",
                 "content": "You are an AI tutor."},
                {"role": "user", "content": "What is AI"}]

response = client.chat.completions.create(
    model="text_demo",  # model = "deployment_name"
    messages=message_text,
    temperature=0.7,
    max_tokens=350,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

print(response)
