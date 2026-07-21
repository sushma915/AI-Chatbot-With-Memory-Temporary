from langchain_core.chat_history import(
    InMemoryChatMessageHistory 
)

from langchain_core.runnables.history import (
    RunnableWithMessageHistory
)

from langchain_core.output_parsers import StrOutputParser

from llm_provider import get_llm 

from prompts import prompt

# create the llm 

llm = get_llm() 

# create output parser 

parser = StrOutputParser() 

# create the chain

chain = (
    prompt 
    | llm 
    | parser
)

# store user histories

store = {}

# get history for a particular session 
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory() 
    return store[session_id]

# create the chain with message history 
chain_with_history = RunnableWithMessageHistory(
    chain, 
    get_session_history, 
    input_messages_key="input", 
    history_messages_key="history"
)