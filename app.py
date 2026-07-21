import streamlit as st

from chains import (
    chain_with_history,
    get_session_history
)


st.set_page_config(

    page_title="AI Chatbot",

    page_icon="🤖"

)


st.title("🤖 AI Chatbot with Memory")


# Create session ID

if "session_id" not in st.session_state:

    st.session_state.session_id = "user1"


# Get user input

user_input = st.chat_input(
    "Type your message..."
)


# Process message

if user_input:

    with st.spinner("🤖 Thinking..."):

        chain_with_history.invoke(

            {
                "input": user_input
            },

            config={

                "configurable": {

                    "session_id": (
                        st.session_state.session_id
                    )

                }

            }

        )


# Get conversation history

history = get_session_history(

    st.session_state.session_id

)


# Display messages

for message in history.messages:

    if message.type == "human":

        with st.chat_message("user"):

            st.write(message.content)


    elif message.type == "ai":

        with st.chat_message("assistant"):

            st.write(message.content)