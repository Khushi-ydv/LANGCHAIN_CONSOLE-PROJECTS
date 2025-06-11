from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents=["Elon Musk is the CEO of SpaceX which is a space exploration company",
           "Bill Gates is the founder of Microsoft multinational technology company that develops and licenses a wide range of software, services, and hardware.",
           "Jeff Bezos is the founder of Amazon, an American multinational technology company that focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence.",
           "Mark Zuckerberg is the co-founder of Facebook, a social media and technology company.",
           "Larry Page and Sergey Brin are the co-founders of Google, a multinational technology company specializing in Internet-related services and products."]
query="Tell me about Microsoft"

#Later on we will store the document embeddings in a vector database like Pinecone or ChromaDB
doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

# Calculate cosine similarity between the query embedding and document embeddings

scores=cosine_similarity([query_embedding] , doc_embeddings)[0]

# print(list(enumerate(scores)))
index , score = sorted(list(enumerate(scores)),key=lambda x: x[1], reverse=True)[0]
print("Query:",query)
print(documents[index])
print("similarity score : ",score)

