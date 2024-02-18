import streamlit as st
import os
from PyPDF2 import PdfReader
import docx
from langchain.text_splitter import CharacterTextSplitter
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# DeepSeek API key
DEEPSEEK_API_KEY = "DEEPSEEK_API_KEY"

# Function to get text from multiple files
def get_files_text(uploaded_files):
    text = ""
    for uploaded_file in uploaded_files:
        split_tup = os.path.splitext(uploaded_file.name)
        file_extension = split_tup[1]
        if file_extension == ".pdf":
            text += get_pdf_text(uploaded_file)
        elif file_extension == ".docx":
            text += get_docx_text(uploaded_file)
        else:
            text += get_csv_text(uploaded_file)  # Assuming you have a get_csv_text function
    return text

# Function to get text from a PDF file
def get_pdf_text(pdf):
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to get text from a DOCX file
def get_docx_text(file):
    doc = docx.Document(file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to rewrite text with DeepSeek
def rewrite_text_with_deepseek(text_chunks):
    rewritten_text_chunks = []
    for chunk in text_chunks:
        # Prepare the request payload
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": "Please rewrite the following text in fluent Persian:"},
                {"role": "assistant", "content": chunk}
            ],
            "temperature": 0.7,
            "max_tokens": 10000,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        # Send the request to DeepSeek
        response = requests.post("https://api.deepseek.com/v1/chat/completions", json=payload, headers=headers)
        # Handle the response
        if response.status_code == 200:
            rewritten_text_chunks.append(response.json()["choices"][0]["message"]["content"])
        else:
            st.error("Error from DeepSeek API: " + response.text)
    return rewritten_text_chunks

# Streamlit app
def main():
    st.title("Document Rewriter with DeepSeek AI write by kiarash[ https://github.com/u10if]")

    # File upload
    uploaded_files = st.file_uploader("Choose files", type=["pdf", "docx", "csv"], accept_multiple_files=True)

    if uploaded_files:
        # Convert files to text
        text = get_files_text(uploaded_files)

        # Split text into chunks
        text_chunks = get_text_chunks(text)

        # Rewrite text with DeepSeek
        rewritten_text_chunks = rewrite_text_with_deepseek(text_chunks)

        # Compile rewritten text into a single string
        rewritten_text = ' '.join(rewritten_text_chunks)

        # Display rewritten text
        st.write("Rewritten Text:")
        st.write(rewritten_text)

        # Provide download link for rewritten text
        st.download_button(
            label="Download Rewritten Text",
            data=rewritten_text.encode('utf-8'),
            file_name="rewritten_text.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()