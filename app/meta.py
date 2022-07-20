HEADER_INFO = """""".strip()
PAGE_INFO = """
<h2 class="font-title">Demo of Abstractive Summarization! </h2>
<p class="strong font-body">
<span class="d-block extra-info">Test how well we summarize your conversation by selecting from one of our test samples or inserting your own into the text box!</span>
</p>
""".strip()
STORY_BARTMEETING = """
<div class="story-box font-body">
<p>
This model is based on a seq2seq architecture with a bidirectional encoder and a single-directional decoder. <br /><br />

The model was trained on a large set of English language documents and customised to generate summaries based on chat dialogues.
</p>
</div>
""".strip()
STORY_PEGASUS = """
<div class="story-box font-body">
<p>
This model is based on a Transformer encoder-decoder architecture, with a pre-training self-supervised objective called gap-sentence generation which mirrors the summarization task. <br /><br />

The model was trained on a large set of English language documents and customised to generate summaries based on CNN/Daily Mail articles.
</p>
</div>
""".strip()
STORY = {
    "bartmeeting": STORY_BARTMEETING,
    "pegasus": STORY_PEGASUS
}