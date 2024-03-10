from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# To control the randomness and creativity of the generatedcls

# text by an LLM, use temperature = 0.0
chat = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

prompt_template = ChatPromptTemplate.from_template(template_string)
var = prompt_template.messages[0].prompt
var = prompt_template.messages[0].prompt.input_variables

customer_style = """American English \
in a calm and respectful tone
"""

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)


print(type(customer_messages))
print(type(customer_messages[0]))
print(customer_messages[0])

customer_response = chat.invoke(customer_messages)
print(customer_response.content)