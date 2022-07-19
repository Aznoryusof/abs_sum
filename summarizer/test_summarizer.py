import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

from datetime import datetime
from summarizer.test_data import *
from summarizer.summarizer_pegasus import PegasusSummarizer
from summarizer.summarizer_bartmeeting import BartMeetingSummarizer


SEED=99

summarizer = PegasusSummarizer() # BartMeetingSummarizer()
summarizer.load()
start_time = datetime.now()
text = test_data4
print("######## Full Text ########", f"{text}")
print("###########################")
summarised_text = summarizer.summarize(text)
print("######## Summarised Text ########")
print(f"{summarised_text}")
print("###########################")
end_time = datetime.now()
time_taken = end_time - start_time
print(f"Time taken to summarise text: {time_taken}")