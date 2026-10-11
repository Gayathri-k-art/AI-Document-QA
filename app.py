import streamlit as st
from pypdf import PdfReader
from docx import Document
import pandas as pd
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

st.title("AI Document Q&A")

api_key = os.getenv("GEMINI_API_KEY")

uploaded_files = st.file_uploader(
    "Upload your documents",
    type=["pdf", "docx", "txt", "csv"],
    accept_multiple_files=True
)

question = st.text_input("Type your question here")

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join(p.extract_text() or "" for p in reader.pages)
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    elif file.name.endswith(".txt"):
        return file.getvalue().decode("utf-8", errors="replace")
    elif file.name.endswith(".csv"):
        return pd.read_csv(file).to_string(index=False)
    return ""

if uploaded_files:
    all_text = ""
    for file in uploaded_files:
        all_text += f"\nFile: {file.name}\n{extract_text(file)}"

    st.success(f"{len(uploaded_files)} file(s) uploaded")

    if question and st.button("Get Answer"):
        if not api_key:
            st.error("GEMINI_API_KEY missing in .env file")
        else:
            client = genai.Client(api_key=api_key)
            prompt = f"""
            Answer only using these documents:
            {all_text[:100000]}

            Question: {question}
            """
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            st.write(response.text)