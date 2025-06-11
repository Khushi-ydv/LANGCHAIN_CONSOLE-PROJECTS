from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
    template='''Please summarise the research paper titled "{paper_input}" with the following specifications :
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1.mathematical details :
    -include mathematical details if present in the paper
    -explain the mathematical concepts in a clear and concise manner
    2. Analogies:
    -use relatable analogies to simplify complex ideas 
    
    if certain information is not available in the paper , respond with " Insufficientiformation" instead of guessing
    ''',
    input_variables=["paper_input", "style_input", "length_input"]
)

template.save('template.json')