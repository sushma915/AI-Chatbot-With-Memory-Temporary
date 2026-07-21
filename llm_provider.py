from langchain_groq import ChatGroq
from config import GROQ_API_KEY 

def get_llm():
    llm = ChatGroq(
        model = "llama-3.3-70b-versatile",
        temperature=0,
        api_key=GROQ_API_KEY
    )
    return llm