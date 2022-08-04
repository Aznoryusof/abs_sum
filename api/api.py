import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

from fastapi import FastAPI, HTTPException, Query
from pydantic import Required


SUMMARIZER_NAME = "bartmeeting"


def load_abs_summarizer(summarizer_name):
    if summarizer_name=="bartmeeting":
        from summarizer.summarizer_bartmeeting import BartMeetingSummarizer as AbsSum
    if summarizer_name=="pegasus":
        from summarizer.summarizer_pegasus import PegasusSummarizer as AbsSum

    abs_summarizer = AbsSum()
    abs_summarizer.load()

    return abs_summarizer


abs_summarizer = load_abs_summarizer(summarizer_name=SUMMARIZER_NAME)
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to Abstractive Summarization API"}


@app.post("/predict")
def predict(text: str = Query(default=Required)):

    if(not(text)):
        raise HTTPException(status_code=400, 
                            detail = "Please Provide a valid text input")

    summary_text = abs_summarizer.summarize(text)
    return {
        "text": text,
        "summary_text": summary_text
    }

