from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import GOOGLE_API_KEY
from utils import load_pdf, split_documents


# Embedding Model


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

persist_directory = "chroma_db"


# Load PDF


documents = load_pdf("data/sample.pdf")

chunks = split_documents(documents)

print(f"Pages Loaded : {len(documents)}")
print(f"Chunks Created : {len(chunks)}")


# Vector Database

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=persist_directory
)

print("✅ ChromaDB created successfully!")


# Retriever


retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

print("✅ Retriever created successfully!")


# Gemini LLM

llm = ChatGoogleGenerativeAI(
    model="models/gemini-3.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)


# Prompt


prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer the question only from the context below.

Context:
{context}

Question:
{question}
""")

chain = prompt | llm | StrOutputParser()


# Function

def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response
