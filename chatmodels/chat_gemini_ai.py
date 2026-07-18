from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv() 

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash",temperature=0.7,max_tokens=200)

result = model.invoke("what is cricket?")
print(result.content)