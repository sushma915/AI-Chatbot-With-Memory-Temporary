from langchain_core.prompts import(
    ChatPromptTemplate,
    MessagesPlaceholder
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a friendly AI assistant.
            Use the conversation history when necessary.
            """
        ),

        MessagesPlaceholder(
            variable_name="history"
        ),
        ("human", "{input}")
    ]
)