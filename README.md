# 🤖 AI Chatbot with Temporary Memory

An interactive AI chatbot built with **Streamlit**, **LangChain**, and **Groq** using the **Llama 3.3 70B** model. This application maintains temporary session-based conversation memory (`InMemoryChatMessageHistory`), allowing the assistant to remember contextual information during active chat sessions.

---

## ✨ Features

- **Context-Aware Responses**: Uses LangChain's `RunnableWithMessageHistory` to track context within session state.
- **Ultra-Fast LLM Inference**: Powered by Groq's high-speed API utilizing `llama-3.3-70b-versatile`.
- **Sleek Web Interface**: Modern, intuitive chat UI built with Streamlit (`st.chat_input` and `st.chat_message`).
- **Modular Codebase**: Clean separation of configuration, LLM initialization, prompt templates, chains, and frontend code.

---

## 🛠️ Tech Stack

- **Framework**: Python 3.10+
- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Orchestration**: [LangChain](https://www.langchain.com/) (`langchain-core`, `langchain-groq`)
- **Model Provider**: [Groq](https://groq.com/) (`llama-3.3-70b-versatile`)
- **Environment Management**: `python-dotenv`

---

## 📁 Project Structure

```text
AI_Chatbot_With_Memory/
├── app.py              # Main Streamlit application and UI logic
├── chains.py           # LangChain RunnableWithMessageHistory setup & session history store
├── config.py           # Environment configuration loader
├── llm_provider.py     # Groq Chat model setup (llama-3.3-70b-versatile)
├── prompts.py          # System prompt template & chat message placeholder
├── requirements.txt    # Required Python dependencies
├── .env                # API keys and secret variables (git-ignored)
├── .gitignore          # Files ignored by Git
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

- Python **3.9+** installed on your system.
- A **Groq API Key**. You can get one for free at [console.groq.com](https://console.groq.com/).

### 2. Installation

1. **Clone the repository** (or navigate to your project directory):
   ```bash
   git clone https://github.com/sushma915/AI-Chatbot-With-Memory-Temporary.git
   cd AI-Chatbot-With-Memory-Temporary
   ```

2. **Create a virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Configuration

Create a `.env` file in the root directory of the project and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ **Note**: Do not commit your `.env` file to public repositories. Ensure it remains in `.gitignore`.

---

## 🏃 Running the Application

Launch the Streamlit web server by running:

```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

---

## 💡 How It Works

1. **Prompt Template (`prompts.py`)**: Defines the chatbot persona and reserves space for chat history via `MessagesPlaceholder(variable_name="history")`.
2. **LLM Provider (`llm_provider.py`)**: Connects to Groq using `ChatGroq` with `llama-3.3-70b-versatile` at `temperature=0` for structured, accurate answers.
3. **Chain & Memory (`chains.py`)**: Combines Prompt, LLM, and `StrOutputParser`. Wraps the chain with `RunnableWithMessageHistory` mapping each session ID to an `InMemoryChatMessageHistory` instance.
4. **User Interface (`app.py`)**: Manages session state, streams user input into the LangChain runnable, and renders human and AI message history.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
