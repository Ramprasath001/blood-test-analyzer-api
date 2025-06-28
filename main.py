# ====================== main.py ======================
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from utils import extract_pdf_text
import uuid
import os

app = FastAPI(title="Simple Blood Test Report Analyzer")

@app.post("/analyze")
async def analyze_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarize my blood report")
):
    try:
        os.makedirs("data", exist_ok=True)
        file_id = str(uuid.uuid4())
        file_path = f"data/{file_id}_{file.filename}"

        with open(file_path, "wb") as f:
            f.write(await file.read())

        text = extract_pdf_text(file_path)

        # Fake summary logic for demo
        summary = "This blood test shows normal levels of most markers. Recommend routine check-up.\n\n" + text[:500]

        return JSONResponse({
            "status": "success",
            "summary": summary,
            "file_processed": file.filename
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

