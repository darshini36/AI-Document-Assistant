# 🤖 AI Document Assistant (RAG)

An AI-powered Document Question Answering application built using **LangChain**, **Google Gemini**, **HuggingFace Embeddings**, **ChromaDB**, and **Streamlit**.

This application allows users to upload or use a PDF document and ask natural language questions. The system retrieves the most relevant information from the document using Retrieval-Augmented Generation (RAG) and generates accurate answers using Google's Gemini LLM.

---

## 🚀 Features

- 📄 Load PDF documents
- ✂️ Split documents into smaller chunks
- 🧠 Generate embeddings using HuggingFace
- 🗄️ Store embeddings in ChromaDB
- 🔍 Retrieve relevant document chunks
- 🤖 Generate answers using Google Gemini
- 🌐 Simple Streamlit web interface

---

## 🏗️ Project Architecture

```
PDF
 │
 ▼
PDF Loader
 │
 ▼
Text Splitter
 │
 ▼
Embeddings (HuggingFace)
 │
 ▼
ChromaDB (Vector Database)
 │
 ▼
Retriever
 │
 ▼
Gemini LLM
 │
 ▼
Answer
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- HuggingFace Embeddings
- ChromaDB
- PyPDF
- python-dotenv

---

## 📁 Project Structure

```
AI-Document-Assistant/
│
├── app.py              # Streamlit UI
├── rag.py              # RAG pipeline
├── utils.py            # PDF loading & text splitting
├── config.py           # API configuration
├── requirements.txt
├── .env                # API Key (ignored by Git)
├── data/
│   └── sample.pdf
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/darshini36/AI-Document-Assistant.git

cd AI-Document-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 💬 Example Questions

- What are my technical skills?
- Where did I complete my internship?
- What programming languages do I know?
- Summarize my resume.
- What projects have I completed?

---

## 📸 Demo

Add screenshots of the application here.

Example:

- Home Page
- Question Answering
- Output Screen

---

## 📌 Future Improvements

- Support multiple PDF uploads
- Chat history
- Source citation for answers
- Voice input
- PDF upload from UI
- Deploy using Streamlit Cloud

---

## 👩‍💻 Author

**Darshini Peddinti**

GitHub: https://github.com/darshini36

LinkedIn: *(https://www.linkedin.com/in/darshini-peddinti-481906290/.)*
