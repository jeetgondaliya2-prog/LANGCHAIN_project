from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct",temperature=0.9,max_tokens=200)

response = model.invoke("what is the capital of India?")
print(response.content)