from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
#Less dimension means less cost and smaller context 
#More dimension means more cost and larger context 
embedding=OpenAIEmbeddings(model='text-embedding-3-large' , dimensions=16)

result=embedding.embed_query("Delhi is capital of India")
print(result)
