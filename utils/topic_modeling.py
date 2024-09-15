from transformers import pipeline

def extract_topics(text):
    # Example using a pipeline, replace with LDA or other methods as needed
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

