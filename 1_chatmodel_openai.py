from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#model=ChatOpenAI(model='gpt-4')

#1st Note
'''temperature is the parameter for deciding the 
creativeness/randomness of your response .
Higher the temperature , more creative or random the response is 
[Alg output milenge for same input ]
->useful for creative tasks like writing poems , stories etc .

lower the temperature , more deterministic or focused the response is
->useful for tasks like question answering, summarization etc. 
[ same input k liye same output milega if temp=0]
'''
#2nd Note
'''max_completion_tokens is used for setting maximum no. of tokens in output 
(Length of response).'''
model=ChatOpenAI(model='gpt-4', temperature=0.5,max_completion_tokens=10)

result=model.invoke("Tell me a joke on engineers")
#print(result)
print(result.content)
