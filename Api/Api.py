import uvicorn
from fastapi import FastAPI, File, UploadFile
from Logic.Logic import *
from Models.Models import *

app = FastAPI(title="staff-learning-assistant-api", version="0.0.1")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/scrape/")
def scrape(scrape_request_body: URLScrapeRequestBody):
    return Logic().url_scrape(scrape_request_body)


@app.post("/scrapeDocument/")
def scrape(files: List[UploadFile]):
    if not files:
        return "error"
    return Logic().document_scrape(files=files)


@app.post("/ask/", response_model=AskResponseBody)
def ask(ask_request_body: AskRequestBody):
    return Logic().ask(ask_request_body.question)


if __name__ == "__main__":
    uvicorn.run("Api:app", host="127.0.0.1", port=5000, log_level="info")