from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st


load_dotenv()
model=ChatOpenAI(model="gpt-4o", max_tokens=20)

st.header("Research Tool")
st.subheader("Summarize your research paper")
#DROP DOWN MENU 
paper_input=st.selectbox(
    "Select a research paper name",["Select ...","Diffusion Models Beat GANs on Image Synthesis","Large Language Models are Zero-Shot Reasoners","Language Models are Few-Shot Learners","Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" , "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context", "Generative Pre-trained Transformer 3 (GPT-3): Language Models are Few-Shot Learners", "ImageNet Classification with Deep Convolutional Neural Networks", "Deep Residual Learning for Image Recognition", "Neural Machine Translation by Jointly Learning to Align and Translate"]
)

style_input=st.selectbox(
    "Select a style",["Select ...","Formal","Informal","Technical","Concise","Descriptive","Mathematical" , "Code-oriented" , "Beginner-friendly"]
)

length_input=st.selectbox(
    "Select a length",["Select ...","Short(1-2 paragraphs)","Medium (3-6 paragraphs)","Long (detailed explanation)"]
)

#template 

# template=PromptTemplate(
#     template='''Please summarise the research paper titled "{paper_input}" with the following specifications :
#     Explanation Style: {style_input}
#     Explanation Length: {length_input}
#     1.mathematical details :
#     -include mathematical details if present in the paper
#     -explain the mathematical concepts in a clear and concise manner
#     2. Analogies:
#     -use relatable analogies to simplify complex ideas 
    
#     if certain information is not available in the paper , respond with " Insufficientiformation" instead of guessing
#     ''',
#     input_variables=["paper_input", "style_input", "length_input"]
# )

template= load_prompt('template.json')

#fill the placeholders
prompt=template.invoke(
    {
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    }
)

# #Single line prompt
# user_input=st.text_input("Enter your prompt here : ")

if st.button("Summarize"):
    result=model.invoke(prompt)
    st.write(result.content)