# deepseek-chatbot by kiarash
This is a Python script that uses the Streamlit library to create a web application for rewriting text from uploaded files using the DeepSeek API. The script imports necessary libraries and defines several functions to handle file uploads, text extraction, text splitting, and text rewriting.
# DeepSeek Document Rewriter

This is a Streamlit-based web application that allows users to upload documents (PDF, DOCX, and CSV) and rewrite the text content using the DeepSeek AI API. The application extracts text from the uploaded files, splits it into chunks, and sends each chunk to the DeepSeek API for rewriting. The rewritten text is then displayed in the app and can be downloaded as a text file.

## Features

- Upload multiple files (PDF, DOCX, and CSV)
- Extract text from uploaded files
- Split text into manageable chunks
- Rewrite text using the DeepSeek AI API
- Display the rewritten text
- Download the rewritten text as a text file

## Requirements

To run this application, you need to have the following libraries installed:

- streamlit
- os
- PyPDF2
- docx
- langchain
- requests
- python-docx (for DOCX support)

You also need to have a DeepSeek API key.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/u10if/deepseek-chatbot.git
```
1. Navigate to the project directory:
```bash
cd deepseek-document-rewriter
```
1. Install the required libraries:
```bash
pip install -r requirements.txt
```
1. Replace `"deepseek api"` in the script with your actual DeepSeek API key.

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```
1. Open your web browser and go to the URL provided by Streamlit.
1. Upload your files (PDF, DOCX, and CSV) by clicking the "Choose files" button.
1. The app will extract the text from the files, split it into chunks, and send each chunk to the DeepSeek API for rewriting.
1. The rewritten text will be displayed in the app.
1. Click the "Download Rewritten Text" button to download the rewritten text as a text file.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
