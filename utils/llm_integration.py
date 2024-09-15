# utils/llm_integration.py

from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

def answer_query(question, context):
    question_answerer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    result = question_answerer(question=question, context=context)
    return result['answer']
