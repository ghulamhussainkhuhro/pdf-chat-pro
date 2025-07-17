import streamlit as st
import os
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.pipeline import load_pdf_text, get_vectorstore, get_qa_chain
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

st.set_page_config(page_title="📚 PDF Chatbot", layout="wide", page_icon="📄")

# Sidebar
with st.sidebar:
    st.title("📄 PDF AI Assistant")
    st.write("Upload a PDF and chat with it using Azure OpenAI.")
    dark_mode = st.checkbox("🌙 Dark Mode", value=True)
    st.markdown("---")
    st.markdown("👨‍💻 Built by [Your Name](#)")

# Main UI
st.title("💬 Chat With Your PDF")
pdf_file = st.file_uploader("📂 Upload your PDF file", type=["pdf"])

if pdf_file:
    temp_pdf_path = f"data/temp_{uuid4().hex}.pdf"
    with open(temp_pdf_path, "wb") as f:
        f.write(pdf_file.read())

    with st.spinner("📥 Loading PDF..."):
        raw_text = load_pdf_text(temp_pdf_path)
        st.success(f"✅ Extracted {len(raw_text)} characters")

    with st.spinner("📚 Generating vectorstore..."):
        vectorstore = get_vectorstore(raw_text)

    with st.spinner("🔗 Setting up QA chain..."):
        qa_chain = get_qa_chain(vectorstore)
        st.success("✅ Chatbot is ready!")

    # Summary block
    with st.expander("🧠 Click to Generate Summary"):
        if st.button("Generate Summary"):
            with st.spinner("Summarizing..."):
                summary_response = qa_chain.invoke({"query": "Please summarize the PDF."})
                st.markdown(f"**📜 Summary:**\n\n{summary_response['result']}")

    # Chat state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        st.session_state.chat_log = []

    st.markdown("### 💬 Ask Questions About Your PDF")
    user_query = st.text_input("🔍 Your question")

    if user_query:
        start_time = time.time()
        result = qa_chain.invoke({"query": user_query})
        end_time = time.time()
        latency = round(end_time - start_time, 2)

        answer = result["result"]
        sources = result.get("source_documents", [])

        st.session_state.chat_history.append((user_query, answer))
        st.session_state.chat_log.append(f"Q: {user_query}\nA: {answer}\nTime: {latency}s\n")

        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):
            st.markdown(answer)
            with st.expander("📄 Source Chunks"):
                for i, doc in enumerate(sources):
                    st.markdown(f"**Source {i+1}:** {doc.page_content[:300]}...")

        st.markdown(f"⏱️ Response time: {latency}s")

    if st.session_state.chat_history:
        st.markdown("---")
        st.markdown("### 💾 Download Logs")
        if st.button("📥 Download Chat Log"):
            log_text = "\n\n".join(st.session_state.chat_log)
            st.download_button(
                label="📄 Download .txt",
                data=log_text,
                file_name="chat_log.txt",
                mime="text/plain"
            )

    # Cleanup
    os.remove(temp_pdf_path)
