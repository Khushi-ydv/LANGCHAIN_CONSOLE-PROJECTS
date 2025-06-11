from langchain_core.messages import SystemMessage , HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

messages=[
    SystemMessage(content="You are a helpful assisstant"),
    HumanMessage(content="What is Langchain in Generative AI ?")
]
result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)