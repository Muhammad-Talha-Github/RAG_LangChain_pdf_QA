import streamlit as st
from rag_pipeline import load_and_split_pdf, create_vector_store
from gemini_utils import query_gemini
import fitz  # PyMuPDF

# Gemini API Key
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Page setup
st.set_page_config(page_title="PDF AI Assistant", layout="centered")

# Styling
st.markdown("""
    <style>
    body { background-color: #f8f9fa; }
    .main { background-color: #ffffff; padding: 20px; border-radius: 12px; }
    .st-emotion-cache-1avcm0n { max-width: 800px; margin: auto; }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 style="text-align:center;">📄 PDF AI Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:18px; color:gray;">Ask questions about any PDF using Gemini + LangChain</p>', unsafe_allow_html=True)

# Upload
pdf_file = st.file_uploader("📎 Upload a PDF", type="pdf")
question = st.text_input("💬 Ask a question about the PDF")

#Sidebar Metadata Setup
pdf_bytes = None
page_count = 0
chunk_count = 0
file_name = None

if pdf_file:
    file_name = pdf_file.name
    pdf_bytes = pdf_file.read()

    with open("temp.pdf", "wb") as f:
        f.write(pdf_bytes)

    doc = fitz.open("temp.pdf")
    page_count = len(doc)
    doc.close()

# Sidebar 
st.sidebar.header("📊 PDF Metadata")
st.sidebar.markdown(f"**📁 File Name:** `{file_name if file_name else 'N/A'}`")
st.sidebar.markdown(f"**📄 Page Count:** `{page_count}`")
st.sidebar.markdown(f"**🔢 Chunks Created:** `{'?' if chunk_count == 0 else chunk_count}`")

#Main Logic
if pdf_file and question:
    with st.spinner("📚 Processing the document..."):
        docs = load_and_split_pdf("temp.pdf")
        chunk_count = len(docs)

        #updating sidebar with actual chunk count
        st.sidebar.markdown(f"**🔢 Chunks Created:** `{chunk_count}`", unsafe_allow_html=True)

        vector_store = create_vector_store(docs)
        retriever = vector_store.as_retriever(search_type="similarity", k=8)

        intro_chunk = docs[0].page_content
        retrieved_chunks = retriever.get_relevant_documents(question)
        context = intro_chunk + "\n\n" + "\n\n".join([doc.page_content for doc in retrieved_chunks])

        prompt = f"""You are a helpful assistant. Use the following context extracted from a PDF to answer the user's question.

Context:
{context}

Question: {question}

Answer:"""

    with st.spinner("🤖 Getting answer from Gemini..."):
        response = query_gemini(prompt, GEMINI_API_KEY)

    st.success(" Answer")
    st.markdown(
        f"<div style='background-color:#f1f3f4; padding:16px; border-radius:10px; color:#333;'>{response}</div>",
        unsafe_allow_html=True
    )

# Footer (Proper layout)
st.markdown("""
<br><hr>
<center>
🚀 Powered by Gemini 1.5 Flash, LangChain & FAISS  
<br>
Made by <strong>Muhammad Talha</strong>  
<a href="https://github.com/Muhammad-Talha-Github" target="_blank">GitHub</a> | 
<a href="https://www.linkedin.com/in/muhammad-talha-221911255/" target="_blank">LinkedIn</a>
</center>
""", unsafe_allow_html=True)
