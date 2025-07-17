import os
from dotenv import load_dotenv
import fitz  # PyMuPDF
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()

# Load PDF
def load_pdf_text(file_path):
    print(f"📄 Loading PDF: {file_path}")
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    print(f"✅ Extracted {len(text)} characters of text.")
    return text

# Split & Embed
def get_vectorstore(text):
    print("🔍 Splitting text into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.create_documents([text])
    print(f"✅ Created {len(chunks)} chunks.")

    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )

    print("📦 Creating FAISS vectorstore...")
    return FAISS.from_documents(chunks, embeddings)

# LLM
def get_qa_chain(vectorstore):
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )

    prompt_template = """
    You are a helpful assistant answering questions based only on the provided document text.

    Context:
    {context}

    Question:
    {question}

    Only answer based on the context above. If the context does not contain the answer, say "I couldn't find the answer in the document."
    """

    prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
