# # pip install streamlit transformers langchain_community
# Also install ollama before running the code and make sure you have phi3 model in your local
from langchain_community.llms import Ollama

def create_post(post_type,ts,length,context):
# Import Ollama module from Langchain
    
    # !ollama pull llama3
    # Initialize an instance of the Ollama model
    llm = Ollama(model="phi3:mini")
    input_prompt = f"Generate a {length} linkedin post.Its a {post_type}.Keep tone and style as {ts}.The post is about {context}"
    # Invoke the model to generate responses
    response = llm.invoke(input_prompt)
    return response
###############################################
# Without langcahin code
# import ollama
# response = ollama.chat(model='phi3:mini', messages=[
#   {
#     'role': 'user',
#     'content': 'Generate Post?',
#   },
# ])
# print(response['message']['content'])