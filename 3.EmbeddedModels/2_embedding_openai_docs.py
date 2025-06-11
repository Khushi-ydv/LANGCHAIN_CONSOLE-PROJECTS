from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
#Less dimension means less cost and smaller context 
#More dimension means more cost and larger context 
embedding=OpenAIEmbeddings(model='text-embedding-3-large' , dimensions=16)
documents=[
    "Delhi is capital of India",
    "Tokyo is capital of Japan",
    "Washington DC is capital of USA",
    "London is capital of UK"
]
result=embedding.embed_documents(documents)
print(result)
