import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

from transformers import pipeline
from summarizer.utils.clean_input_text import clean_input_text


class BartMeetingSummarizer:
    def __init__(self):
        self.debug = False
        self.summarizer = None
        self.model_name_or_path = "knkarthick/MEETING_SUMMARY"

    
    def load(self):
        self.summarizer = pipeline("summarization", model=self.model_name_or_path)


    def summarize(self, text):
        text_clean = clean_input_text(text)
        summary_text = self.summarizer(
            text_clean, max_length=200, 
            min_length=5, do_sample=False
        )[0]["summary_text"]

        return summary_text