from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel , Field
from typing import TypedDict , Annotated , Optional , Literal

#-----------1. OPEN AI API --------------------
load_dotenv()
model=ChatOpenAI()

#schema for structured output

class Review(BaseModel):
    key_themes :list[str]= Field(description="Key themes of the review")
    summary : str = Field(description="A brief summary of review")
    sentiment : Literal["pos","neg"] =Field(description="Sentiment of the review, either pos or neg")
    pros : Optional[list[str]] = Field(default=None, description="List of pros mentioned in the review")
    cons : Optional[list[str]] = Field(default=None, description="List of cons mentioned in the review")
    name:Optional[str] = Field(default=None, description="Name of the reviewer")
    
    
#invoke the model with structured output
structured_model=model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is good , but the software feels bloated . there are too many pre-installed apps that i cant removr . 
                    Also the UI looks outdated and not user-friendly compared to other brands 
                    Hoping for a software update to fix this ,
                    """)
print(result)
