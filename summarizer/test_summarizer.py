import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

from datetime import datetime
from transformers import pipeline
from summarizer.test_data import *


SEED=99
MODEL_NAME = "knkarthick/MEETING_SUMMARY"

summarizer = pipeline("summarization", model=MODEL_NAME)
start_time = datetime.now()
text = test_data4
print("######## Full Text ########", f"{text}")
print("###########################")
summarised_text = summarizer(text, max_length=200, min_length=5, do_sample=False)[0]["summary_text"]
print("######## Summarised Text ########")
print(f"{summarised_text}")
print("###########################")
end_time = datetime.now()
time_taken = end_time - start_time
print(f"Time taken to summarise text: {time_taken}")