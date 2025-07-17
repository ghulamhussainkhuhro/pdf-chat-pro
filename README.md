# 📄 PDF Chatbot – Talk to Your PDFs with AI

A production-ready, Azure-powered PDF chatbot that lets you upload any PDF and chat with it using natural language. Built using **LangChain**, **FAISS**, and **Azure OpenAI**, this tool demonstrates strong engineering skills in **AI integration**, **vector search**, and **interactive NLP applications**.

---

## 🔍 Features

- ✅ **Upload Any PDF** – Seamlessly extract content via PyMuPDF  
- 💬 **Natural Chat Interface** – Ask contextual questions and get accurate answers  
- 🧠 **Smart Summarization** – Generate instant summaries with a single click  
- 📚 **Source-Aware Responses** – View document chunks that support the answers  
- ⏱️ **Latency Tracking** – Measure response time for each query  
- 🌗 **Dark/Light Mode Toggle** – Professional UI using Streamlit theming  
- 📥 **Download Chat Logs** – Save your Q&A sessions as `.txt` files  

---

## 🛠️ Tech Stack

| Area         | Tools Used                                 |
|--------------|---------------------------------------------|
| LLM Backend  | Azure OpenAI (ChatGPT + Embeddings)         |
| Vector Store | FAISS                                       |
| PDF Parsing  | PyMuPDF (fitz)                              |
| App Logic    | LangChain, RetrievalQA                      |
| Frontend     | Streamlit (Custom UI with chat experience)  |
| Utilities    | Python, dotenv, UUID, CLI support           |

---

## 📁 Project Structure

```
pdf-chat-pro/
├── app/
│   ├── main.py              # CLI-based PDF Q&A
│   └── streamlit_app.py     # Interactive web app
├── backend/
│   ├── __init__.py
│   └── pipeline.py          # Core PDF parsing, embeddings, QA chain
├── data/
│   └── Introduction_to_AI_Assistants.pdf  # Sample PDF
├── test-pipeline.py         # Script for testing pipeline logic
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/pdf-chat-pro.git && cd pdf-chat-pro

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your Azure OpenAI keys in a .env file
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_DEPLOYMENT=...
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=...
AZURE_OPENAI_API_VERSION=...

# 4. Run CLI app
python app/main.py

# OR: Run the Streamlit web app
streamlit run app/streamlit_app.py
```

---

## 🎯 Why This Project

This project reflects practical, production-grade experience combining **AI**, **data pipelines**, and **user-focused design**. Whether you're analyzing legal documents, research papers, or resumes — this app brings the power of conversational AI to any PDF.

---

## 👨‍💻 About Me

**Ghulam Hussain Khuhro**  
AI/ML Engineer · Data Scientist · Google-Certified Data Analyst  
📬 ghulamhussain.developer@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/ghulamhussainkhuhro/) • [GitHub](https://github.com/ghulamhussainkhuhro/) • [Portfolio](https://ghulamhussainkhuhro.github.io/)

---

If this project interests you or you'd like to collaborate, feel free to connect. Feedback and contributions are always welcome!
