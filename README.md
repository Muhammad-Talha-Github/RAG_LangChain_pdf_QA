# 📄 PDF AI Assistant — Ask Your PDFs Using Gemini 1.5 + LangChain

This is an intelligent, modern, and free-to-use Streamlit web app that allows you to ask **natural language questions** about any PDF — like research papers, reports, or textbooks — powered by:

- 🔍 Retrieval-Augmented Generation (RAG)
- 💬 Google Gemini 1.5 Flash (via API)
- 🧠 LangChain + FAISS for document chunking & vector search
- ⚙️ Clean, professional, and interactive UI built with Streamlit

---

## 🚀 Features

- 📎 Upload any PDF file
- 💡 Ask any question about the document
- 🔍 Context-aware answers using Gemini + retrieved chunks
- 📊 Sidebar shows:
  - PDF file name
  - Total page count
  - Number of content chunks used
- 📱 Responsive and modern UI
- 💡 Optimized for research papers (e.g., “Attention Is All You Need”)

---

## 🛠️ Tech Stack

| Layer           | Tool/Library            |
|----------------|--------------------------|
| LLM             | [Gemini 1.5 Flash](https://ai.google.dev) |
| RAG + Embeddings | [LangChain](https://github.com/langchain-ai/langchain), FAISS |
| PDF Parsing     | PyMuPDF (fitz), LangChain loaders |
| Web UI          | [Streamlit](https://streamlit.io/) |
| Chunking        | RecursiveCharacterTextSplitter |

---

## 🧪 Example Questions (for research papers)

Here are some example questions you can ask for a paper like **"Attention Is All You Need"**:

- 🧠 What is the main contribution of this paper?
- ⚙️ How does self-attention work in Transformers?
- 📈 What results did the model achieve?
- 🔄 What makes this architecture different from LSTMs?
- 💡 How did this paper influence later models like BERT or GPT?

---

## 🔐 Setup Instructions

> ✅ **100% Free to Run** — all tools and APIs used have free tiers.

### 1. Clone this repository

```bash
git clone https://github.com/your-username/pdf-gemini-assistant.git
cd pdf-gemini-assistant
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Open `app.py` and replace the placeholder:

```python
GEMINI_API_KEY = "your-gemini-api-key-here"
```

You can get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📸 Screenshots


---

## 👨‍💻 Developed By

**Muhammad Talha**

* 🌐 [GitHub](https://github.com/Muhammad-Talha-Github)
* 💼 [LinkedIn](https://www.linkedin.com/in/muhammad-talha-221911255/)
