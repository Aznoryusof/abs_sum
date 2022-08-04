import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(main_dir)


def clean_input_text(input_text):
    clean_output = " ".join([x.strip() for x in input_text.split(" ") if x.strip() != ""])
    clean_output = "\n" + clean_output
    return clean_output