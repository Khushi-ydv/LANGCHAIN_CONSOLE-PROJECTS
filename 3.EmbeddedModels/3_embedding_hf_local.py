from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
'''
#Example for textembedding

text="Delhi is capital of India"
result=embedding.embed_query(text)
'''
#Example for document embedddings

documents=[
    "Delhi is capital of India",
    "Tokyo is capital of Japan",
    "Washington DC is capital of USA",
    "London is capital of UK"
]
result=embedding.embed_documents(documents)
print(result)
