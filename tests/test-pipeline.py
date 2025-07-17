import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.pipeline import load_pdf_text, get_vectorstore, get_qa_chain


def main():
    file_path = "data/Resume_Ghulam_Hussain_Khuhro.pdf"
    text = load_pdf_text(file_path)
    vectorstore = get_vectorstore(text)
    qa_chain = get_qa_chain(vectorstore)

    print("🧠 Ready to answer questions.")
    while True:
        question = input("Ask a question (or 'exit'): ")
        if question.lower() == "exit":
            break
        result = qa_chain.invoke({"query": question})
        print("🗣️ Answer:", result["result"])
        print()

if __name__ == "__main__":
    main()
