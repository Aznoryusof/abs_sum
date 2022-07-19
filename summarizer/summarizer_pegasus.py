import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

from transformers import PegasusForConditionalGeneration, PegasusTokenizer

PEGASUS_MODEL = "sshleifer/distill-pegasus-cnn-16-4" 
PEGASUS_TOKENIZER = "sshleifer/distill-pegasus-cnn-16-4"


class PegasusSummarizer:
    def __init__(self):
        self.torch_device = 'cpu'
        self.tokenizer = PegasusTokenizer.from_pretrained(PEGASUS_TOKENIZER)
        self.model = PegasusForConditionalGeneration.from_pretrained(PEGASUS_MODEL).to(self.torch_device)

    def summarize(self, text):
        src_text = text
        tokens = self.tokenizer(src_text, truncation=True, padding='longest', return_tensors='pt').to(self.torch_device)
        summarized = self.model.generate(**tokens)
        summarized_text = self.tokenizer.batch_decode(summarized, skip_special_tokens=True)
        return summarized_text