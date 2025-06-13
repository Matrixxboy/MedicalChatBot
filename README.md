
# 🧠 MedicalChatBot

> A smart, safe, and context-aware **AI Medical Assistant** trained on your own PDF knowledge base. Built with **LangChain**, **Groq (LLaMA-3)**, **Pinecone**, and **Flask**.

---

## 🚀 Features

- 💬 Ask **medical-related questions** only  
- 📄 Trained on any medical PDF (e.g., The Gale Encyclopedia of Alternative Medicine)  
- ⚡ Powered by **LLaMA-3 via Groq** – blazing fast responses  
- 🔍 Smart retrieval with **Pinecone vector database**  
- 🌙 **Dark & modern UI** for natural conversation  
- 🔐 Secure API key management via `.env`  
- 🔧 Easy to customize, modular structure  

---

## 🗂 Project Structure

```bash
MedicalChatBot/
├── app.py                 # Flask app for the UI
├── storeIndex.py          # Embeds and stores PDF data into Pinecone          
├── requirements.txt       # Project dependencies
├── .env                   # API keys (GROQ + Pinecone)

├── Data/                  # 📄 Add your own medical PDFs here
├── static/
│   └── style.css          # 🌙 Dark aesthetic chatbot styling
├── templates/
│   └── index.html         # 🖥 Chat UI page

└── src/
    └── helper.py          # PDF loading, text splitting, embeddings
    └── prompt.py          # Custom system prompt for medical responses
    └── __init__.py
````

---

## ⚙️ Setup & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Matrixxboy/MedicalChatBot.git
cd MedicalChatBot
```

---

### 2️⃣ Install Requirements

```bash
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

---

### 3️⃣ Add API Keys

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your-groq-api-key
PINECONE_API_KEY=your-pinecone-api-key
```

---

### 4️⃣ Add Your PDF Knowledge Base

Place any medical-related PDFs inside the `Data/` folder.

📌 This changes the **domain** of your chatbot depending on the file.

---

### 5️⃣ Embed the Documents

```bash
python storeIndex.py
```

This will extract, split, embed, and upload your content to Pinecone.

---

### 6️⃣ Run the Chat App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 How It Works

1. **PDFs** ➜ extracted using PyMuPDF
2. Text is **split** into small chunks
3. Chunks are **embedded** using HuggingFace MiniLM
4. **Stored in Pinecone** (vector DB)
5. On user query:

   * Retrieves relevant chunks
   * Sends them + question to **Groq’s LLaMA-3** via a smart prompt
   * Displays concise, medical-safe response

---

## ✨ Prompt Customization

The prompt is defined in `prompt.py`. Example:

```python
  "You are a helpful, smart, and safety-aware AI assistant."
    "You only answer the medical related answers"
    "You are an assistant for question answering task."
    "use the following piece of retrieved context answer"
    "the question If you don't know the answer , say that you"
    "don't know.Use one sentences maximum and keep the"
    "answer concise"
```

Feel free to adjust tone or safety level.

---

## 📸 UI Preview

> Dark theme + chat bubbles for a modern, minimalist look.

*Add your screenshot here*

---

## 🛡 Security Notice

> This repo uses **GitHub Push Protection**.
> API keys inside `.env` are **not allowed to be pushed**.

If a push is blocked:

* Check `.env`, `.ipynb`, or other files for leaked secrets
* Rewrite commit history or use GitHub’s UI to unblock

---

## 🤝 Contributing

Pull requests and feedback are welcome. Let’s improve healthcare tech together! 🩺

---
