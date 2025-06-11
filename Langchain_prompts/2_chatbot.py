from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()
# chat_history=[]
chat_history=[
    SystemMessage(content="You are a helpful assistant"),
    
]

while True :
    user_input = input("You : ")
    # chat_history.append(user_input)
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    else:
        result=model.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print("AI : " , result.content)
print("Chat History: ", chat_history)
