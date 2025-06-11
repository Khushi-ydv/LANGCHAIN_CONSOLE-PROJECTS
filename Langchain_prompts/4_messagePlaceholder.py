from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
#from langchain_core.messages import HumanMessage , SystemMessage , AIMessage
#chat template

chat_template=ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant"),
        # 1Note
        #Agar MsgPlaceholder use ni krenge to System samjh ni payega ki user ki query kis context me h..
        
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}")
    ])

#load chat history

chat_history=[]
with open("4_chathistory.txt") as file:
    chat_history.extend(file.readlines())
print(chat_history)

#create prompt

prompt=chat_template.invoke({
    'chat_history': chat_history,'query': "Where is my refund"
})

print(prompt)