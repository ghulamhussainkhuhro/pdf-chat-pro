# app/main.py

import sys
import os

# Add root project directory to sys.path so backend is discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.pipeline import load_pdf_text, get_vectorstore, get_qa_chain


def main():
    print("📥 Loading PDF...")
    text = load_pdf_text("data/Resume_Ghulam_Hussain_Khuhro.pdf")

    print("📚 Generating vectorstore...")
    vectorstore = get_vectorstore(text)

    print("🔍 Setting up question-answering chain...")
    qa = get_qa_chain(vectorstore.as_retriever())

    print("🧠 Ready to answer questions!")
    while True:
        query = input("Ask a question (or type 'exit' to quit): ")
        if query.lower() in ["exit", "quit"]:
            break

        result = qa.invoke({"query": query})
        print("🗣️ Answer:", result["result"])

        for i, doc in enumerate(result.get("source_documents", [])):
            print(f"\n📄 Source Chunk {i+1}:\n{doc.page_content[:300]}...\n{'-'*40}")


if __name__ == "__main__":
    main()
