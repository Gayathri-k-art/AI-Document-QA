# AI-Based Multi-Document Question Answering System

## 1. Introduction

The AI-Based Multi-Document Question Answering System is an intelligent document processing application designed to help users retrieve information from multiple documents through natural language questions.

In many situations, users need to read large documents to find specific information. Searching manually through multiple files can be difficult, time-consuming, and inefficient.

To solve this problem, this project provides an AI-powered solution where users can upload multiple documents in different formats and ask questions related to their content.

The application extracts text from the uploaded documents, combines the extracted information, and sends the relevant document context along with the user's question to Google Gemini AI. The model processes the provided information and generates a response that is displayed through a simple web interface.

The main goal of this project is to make document understanding easier, faster, and more accessible.

## 2. Problem Statement

Organizations, students, researchers, and professionals frequently work with different types of documents such as PDF reports, Word documents, text files, and spreadsheets.

Finding specific information from these documents creates several challenges:

- Manually reading lengthy documents requires considerable time.
- Searching across multiple files can be difficult.
- Important information may be missed during manual searching.
- Users may need to switch between different documents to understand related information.
- Traditional keyword searching may not provide answers in a natural question-and-answer format.

Therefore, an intelligent system is required that can process multiple documents and allow users to interact with their content using natural language.

This project addresses these challenges by integrating document text extraction with Google Gemini AI.

## 3. Project Objectives

The primary objectives of this project are:

1. **Multiple Document Support:** Allow users to upload multiple documents at the same time.

2. **Document Text Extraction:** Extract readable text from different document formats such as PDF, DOCX, TXT, and CSV.

3. **AI-Based Question Answering:** Use Google Gemini AI to generate answers based on the uploaded document content.

4. **Natural Language Interaction:** Allow users to ask questions using simple and natural language instead of searching manually.

5. **User-Friendly Interface:** Develop an easy-to-use application using Streamlit.

6. **Time Efficiency:** Reduce the time required to search and understand information from multiple documents.

7. **Context-Based Responses:** Provide the extracted document content as context to the AI model so that it can generate document-related answers.

## 4. Project Scope

The project focuses on building a document question-answering application that supports multiple file uploads and AI-based response generation.

The current implementation includes:

- Uploading multiple documents.
- Extracting text from supported file formats.
- Combining extracted text from all uploaded files.
- Accepting questions from users.
- Sending document context and questions to Google Gemini AI.
- Displaying generated answers through a web application.

The application can be useful for students, researchers, office employees, and other users who frequently work with digital documents.

## 5. Key Features

### 5.1 Multiple Document Upload

Users can upload multiple documents in a single session instead of processing each document separately.

The application currently supports:

- PDF files
- DOCX files
- TXT files
- CSV files

### 5.2 Automatic Text Extraction

The application identifies the uploaded file format and uses the appropriate Python library to extract its text content.

### 5.3 AI-Powered Question Answering

Google Gemini AI is integrated to understand the provided document context and generate answers to user questions.

### 5.4 Natural Language Queries

Users can enter questions in simple English without needing to know technical search commands.

### 5.5 Combined Document Context

Text extracted from all uploaded files is combined into a single context. This allows the model to consider information from multiple uploaded documents when generating an answer.

### 5.6 Simple User Interface

Streamlit provides a straightforward interface containing a document uploader, question input field, answer button, and response display area.

## 6. Technologies and Tools Used

### 6.1 Python

Python is the main programming language used to develop the application.

It is responsible for:
- Processing uploaded files.
- Extracting document text.
- Managing application logic.
- Connecting the application with the Gemini API.
- Handling user questions and responses.

### 6.2 Streamlit

Streamlit is used to create the web-based user interface.

It provides:
- Application title and layout.
- Multiple file upload functionality.
- Text input for user questions.
- Buttons for submitting questions.
- Success and error messages.
- Display of AI-generated responses.

### 6.3 Google Gemini AI

Google Gemini AI is the language model used for answer generation.

The application uses the `gemini-2.5-flash` model.

Its responsibilities include:
- Processing the document context.
- Understanding the user's question.
- Generating natural language responses.
- Providing answers based on the supplied information.

### 6.4 PyPDF

PyPDF is used to read PDF files and extract text from individual pages.

The extracted page content is combined into a single text string.

### 6.5 python-docx

The python-docx library is used to read Microsoft Word DOCX files.

It extracts paragraph text from the uploaded Word document.

### 6.6 Pandas

Pandas is used to process CSV files.

The CSV content is converted into a readable text representation that can be included in the document context.

### 6.7 python-dotenv

The python-dotenv library loads environment variables from the `.env` file.

It is used to securely manage the Gemini API key without directly writing the key into the application source code.

## 7. System Architecture

The application follows a document-processing and AI-based question-answering workflow.

### Architecture Components

**1. User Interface Layer**

The user interacts with the application through Streamlit.

This layer allows users to:
- Upload multiple documents.
- Enter questions.
- Submit questions.
- View generated answers.

**2. Document Processing Layer**

This layer identifies the file extension and selects the appropriate extraction method.

Different libraries are used for different document formats.

**3. Text Aggregation Layer**

The extracted text from uploaded documents is combined into one text context.

The current application limits the context sent to the model to the first 100,000 characters.

**4. AI Processing Layer**

The combined document context and user question are passed to Google Gemini AI through the Google GenAI SDK.

**5. Response Generation Layer**

Gemini processes the supplied information and generates a natural language response.

**6. Output Layer**

The generated answer is displayed to the user using Streamlit.

### System Workflow

```text
          User
           |
           v
   Streamlit Interface
           |
           v
   Upload Multiple Files
           |
           v
   File Type Identification
           |
           v
    Document Processing
           |
     +-----+-----+
     |     |     |
    PDF   DOCX   TXT / CSV
     |     |     |
     +-----+-----+
           |
           v
     Text Extraction
           |
           v
    Combine Document Text
           |
           v
     Enter User Question
           |
           v
   Google Gemini AI Model
           |
           v
    Generate AI Response
           |
           v
    Display Answer
```

## 8. Project Folder Structure

The project follows a simple and organized folder structure.

```text
ai-document-q/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── .env
│
└── .gitignore
```

### File Description

**app.py**

Contains the main application code, including:
- Streamlit interface.
- File upload functionality.
- Document text extraction.
- Gemini API integration.
- Question processing.
- Answer display.

**requirements.txt**

Contains the Python dependencies required to run the project.

**README.md**

Provides project documentation, including its overview, architecture, setup instructions, workflow, and future enhancements.

**.env**

Stores the Gemini API key as an environment variable.

**.gitignore**

Specifies files and folders that should not be uploaded to the GitHub repository, such as API credentials and Python cache files.

## 9. Detailed Working Process

### Step 1: Application Initialization

When the application starts, the required Python libraries are imported.

The `load_dotenv()` function loads the environment variables from the `.env` file.

The Gemini API key is retrieved using:

```python
api_key = os.getenv("GEMINI_API_KEY")
```

The Streamlit application displays the title and document upload interface.

### Step 2: Document Upload

The `st.file_uploader()` function allows users to select multiple documents.

The application accepts PDF, DOCX, TXT, and CSV formats.

The `accept_multiple_files=True` option enables multiple file uploads.

### Step 3: File Type Identification and Text Extraction

The `extract_text()` function checks the file extension and selects the appropriate extraction method.

**PDF Processing:**

The `PdfReader` class reads the PDF document. The application extracts text from each page and combines the extracted content.

**DOCX Processing:**

The `Document` class reads Word documents and extracts text from their paragraphs.

**TXT Processing:**

The uploaded text file is read using its byte content and decoded into a readable string.

**CSV Processing:**

Pandas reads the CSV file and converts its contents into a string representation.

### Step 4: Combining Document Content

After extracting text from individual files, the application combines their content into a single variable called `all_text`.

The original file names are also included in the combined context to identify the source document.

This allows information from multiple uploaded files to be provided together to the AI model.

### Step 5: User Question Input

The user enters a question using the Streamlit text input field.

The application waits until the user enters a question and clicks the Get Answer button.

### Step 6: API Key Validation

Before communicating with Gemini, the application checks whether the API key is available.

If the API key is missing, an error message is displayed.

Otherwise, a Gemini client is initialized using the API key.

### Step 7: Prompt Construction

The application creates a prompt containing the extracted document content and the user's question.

The prompt instructs the AI model to answer using only the supplied documents.

To manage the amount of text sent to the model, the application currently uses the first 100,000 characters of the combined document content.

### Step 8: AI Response Generation

The application sends the prompt to the Google Gemini model using the `generate_content()` method.

The model processes the supplied document content and question to generate a response.

### Step 9: Displaying the Answer

The generated response is retrieved from the model output and displayed through Streamlit.

The user can read the response directly in the application.

## 10. Installation and Setup Instructions

### Prerequisites

Before running the application, ensure that the following are available:

- Python 3.10 or a compatible version.
- Visual Studio Code or another Python development environment.
- Internet connection.
- Google Gemini API key.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Directory

```bash
cd ai-document-q
```

### Step 3: Install Dependencies

Install all the required Python packages using:

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory.

Add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with a valid Gemini API key.

Do not upload the actual API key to GitHub.

### Step 5: Run the Application

Execute the following command:

```bash
python -m streamlit run app.py
```

Streamlit starts the application and provides a local URL in the terminal.

Open that URL in a browser to access the application.

## 11. Testing and Expected Results

The application should be tested with different document formats to verify the extraction and question-answering functionality.

| Test Case | Expected Result |
|---|---|
| Upload a PDF | PDF text should be extracted |
| Upload a DOCX | Word document text should be extracted |
| Upload a TXT | Text content should be read |
| Upload a CSV | CSV data should be converted into text |
| Upload multiple files | Text from all uploaded files should be combined |
| Enter a question | Question should be accepted |
| Submit a question | Gemini should generate a response |
| Missing API key | An error message should be displayed |

The expected output is a natural language answer generated using the content supplied from the uploaded documents.

## 12. Limitations

The current implementation has some limitations:

1. **No Vector Database:** The application does not currently store document embeddings in a vector database.

2. **No Semantic Retrieval:** It sends combined document text directly to Gemini rather than retrieving only the most relevant document chunks.

3. **Context Length:** The current implementation sends up to 100,000 characters of combined document text to the model.

4. **Text-Based Extraction:** The application extracts readable text and does not currently implement OCR for scanned documents or images.

5. **DOCX Extraction:** The current implementation extracts paragraph text and does not separately process tables, images, or embedded objects.

6. **CSV Processing:** CSV data is converted into a text representation before being sent to Gemini.

7. **API Dependency:** The application requires a valid Gemini API key and internet connectivity to generate answers.

## 13. Future Enhancements

The project can be improved by introducing additional capabilities.

### 13.1 Document Chunking

Large documents can be divided into smaller text chunks to improve document processing and information handling.

### 13.2 Embedding Generation

Text chunks can be converted into numerical vector representations using an embedding model.

### 13.3 Vector Database Integration

A vector database can be introduced to store document embeddings and support efficient similarity searches.

### 13.4 Semantic Retrieval

The system can retrieve the most relevant document chunks based on the meaning of the user's question instead of passing the entire document content to the model.

### 13.5 Complete RAG Architecture

The application can be extended into a complete Retrieval-Augmented Generation (RAG) system by combining document chunking, embedding generation, vector storage, semantic retrieval, and AI-based response generation.

### 13.6 Chat History

Previous questions and answers can be stored to allow users to review their interactions.

### 13.7 Additional File Formats

Support can be extended to additional document formats and scanned documents through OCR integration.

### 13.8 Improved User Experience

Additional features such as document management, source references, response formatting, and progress indicators can improve usability.

## 14. Applications and Use Cases

The system can be useful in several areas:

- **Education:** Students can upload study materials and ask questions about their content.
- **Research:** Researchers can explore information from multiple research documents.
- **Business:** Employees can retrieve information from reports and business documents.
- **Documentation:** Users can quickly understand lengthy documents.
- **Information Retrieval:** Users can locate relevant information without manually reading every file.

## 15. Conclusion

The AI-Based Multi-Document Question Answering System demonstrates how artificial intelligence can simplify document understanding and information retrieval.

By combining Python, Streamlit, document-processing libraries, and Google Gemini AI, the application provides an interactive way to ask questions about multiple uploaded documents.

The project successfully integrates different document formats, automatic text extraction, and AI-powered answer generation into a single web-based application.

The current implementation provides a foundation that can be further developed into a complete Retrieval-Augmented Generation system by introducing document chunking, embeddings, vector databases, and semantic retrieval.

Overall, this project demonstrates the practical use of Generative AI in building intelligent document-processing applications.