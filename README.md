# Blood Test Analyzer API

A FastAPI-based project that accepts a blood test PDF report and returns a summarized analysis. This project is submitted for the Wingify (VWO) Generative AI Internship Assignment.

---

## Bugs Found and How I Fixed Them

### 1. CrewAI Dependency Errors

* Issues: `crewai`, `crewai-tools`, `BaseTool`, and `Agent` caused Pydantic errors, broken imports, and version conflicts.
* Fix: Removed CrewAI, rebuilt logic using plain FastAPI and LangChain-compatible utilities.

### 2. PDF Parsing Failed

* Issues: Original code used outdated `PDFLoader`, which failed to extract readable content.
* Fix: Switched to `PyPDFLoader` from `langchain_community.document_loaders`.

### 3. Multipart Upload Error

* Issues: FastAPI file upload failed due to missing `python-multipart`.
* Fix: Installed `python-multipart` and updated `requirements.txt`.

### 4. No Root Route

* Issues: Visiting `/` returned `{ "detail": "Not Found" }`.
* Fix: Added a basic root route with a welcome message pointing to `/docs`.

### 5. Tool Compatibility

* Issues: `FileReadTool`, `SerperDevTool`, and others were missing or unstable.
* Fix: Replaced with a custom file reading utility to handle PDF input directly.

---

## Setup and Usage Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/blood-test-analyzer-api.git
cd blood-test-analyzer-api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI Server

```bash
python -m uvicorn main:app --reload
```

### 5. Use the API

Open your browser and visit:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Use the `/analyze` endpoint to upload a PDF and get a summary.

---

## API Documentation

### POST `/analyze`

* Purpose: Accept a PDF file and return a summary of blood report content.
* Method: POST
* Inputs:

  * `file`: PDF file (required)
  * `query`: Optional custom instruction
* Returns: JSON response with summary and filename

Example Response:

```json
{
  "status": "success",
  "summary": "Summary of the blood test...",
  "file_processed": "blood_test_report.pdf"
}
```

---

## Project Structure

```
blood-test-analyzer-api/
├── main.py
├── utils.py
├── requirements.txt
├── README.md
└── data/
    ├── sample.pdf
    └── blood_test_report.pdf
```

---

## Tools and Technologies Used

* Language: Python 3.10
* Framework: FastAPI
* PDF Reader: LangChain (PyPDFLoader)
* Package Manager: pip
* Development Environment: Windows 10
* Editor: Sublime Text
* Terminal: Command Prompt (CMD)
* AI Assistant: ChatGPT (used for debugging and fixes)

---

## Author

Ram Prasath
Internship Submission for Wingify (VWO) Generative AI Program
