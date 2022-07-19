import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

import streamlit as st
from summarizer.test_data import *
from examples import EXAMPLES
import meta
from utils.st import (
    remote_css,
    local_css
)

SEED=99
SUMMARIZER_NAME = "bartmeeting" # or "pegasus"


@st.cache(allow_output_mutation=True)
def load_abs_summarizer(summarizer_name):
    if summarizer_name=="bartmeeting":
        from summarizer.summarizer_bartmeeting import BartMeetingSummarizer as AbsSum
    if summarizer_name=="pegasus":
        from summarizer.summarizer_pegasus import PegasusSummarizer as AbsSum

    abs_summarizer = AbsSum()
    abs_summarizer.load()

    return abs_summarizer


def main(summarizer_name):
    st.set_page_config(
        page_title="Dialogue Summarization",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    abs_summarizer = load_abs_summarizer(summarizer_name=summarizer_name)
    
    remote_css("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Poppins:wght@600&display=swap")
    local_css(main_dir + "/app/asset/css/style.css")

    col1, col2 = st.columns([6, 4])
    with col2:
        with st.expander("Expand to view details about the model", expanded=True):
            st.markdown(meta.STORY, unsafe_allow_html=True)

    with col1:
        st.markdown(meta.HEADER_INFO, unsafe_allow_html=True)
        st.markdown(meta.PAGE_INFO, unsafe_allow_html=True)

        prompts = list(EXAMPLES.keys()) + ["Custom"]
        prompt = st.selectbox(
            'Examples (select from this list)',
            prompts,
            index=0
        )

        if prompt == "Custom":
            prompt_box = ""
        else:
            prompt_box = EXAMPLES[prompt]

        full_text = st.text_area(
            'Insert the text to summarize here: ',
            prompt_box
        )
        entered_text = st.empty()

    summarize_button = st.button('Summarize!')

    st.markdown(
        "<hr />",
        unsafe_allow_html=True
    )
    if summarize_button:
        entered_text.markdown("**Full Text to Summarize:**\n" + full_text)
        with st.spinner("Generating summary..."):
            
            if not isinstance(full_text, str) or not len(full_text) > 1:
                entered_text.markdown(
                    f"Enter text to summarize"
                )
            else:
                summarized_text = abs_summarizer.summarize("\n" + full_text)       
                st.markdown("**Summarized Text:**\n" + summarized_text)


if __name__ == '__main__':
    main(summarizer_name=SUMMARIZER_NAME)


