from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from pathlib import Path
#Optional is used to make a field optional in TypedDict
#Optional me Agar vo value ni milegi to Hallucinations ni aayegi
from typing import TypedDict , Annotated , Optional

#-----------1. OPEN AI API --------------------
load_dotenv()
model=ChatOpenAI()

#schema for structured output

class Review(TypedDict):
    key_themes:Annotated[list[str],"Key themes of the review"]
    summary :Annotated[str,"A brief summary of review"]
    sentiment:str
    pros:Annotated[Optional[list[str]],"List of pros mentioned in the review"]
    cons:Annotated[Optional[list[str]],"List of cons mentioned in the review"]
    
#invoke the model with structured output
structured_model=model.with_structured_output(Review)



result = structured_model.invoke("""The hardware is good , but the software feels bloated . there are too many pre-installed apps that i cant removr . 
                    Also the UI looks outdated and not user-friendly compared to other brands 
                    Hoping for a software update to fix this ,
                    """)
print(result)



#-----------2. OPEN SOURCE API --------------------

# env_path = Path(__file__).resolve().parent.parent / ".env"
# load_dotenv(dotenv_path=env_path)
# print("Token loaded:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))
# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN") 
    
# )
# result=llm.invoke("What is capital of germany")
# print(result)
