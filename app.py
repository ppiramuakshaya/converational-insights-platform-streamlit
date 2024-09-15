import streamlit as st
import os
from utils.transcription import transcribe_audio
from utils.topic_modeling import extract_topics
from utils.sentiment_analysis import analyze_sentiment
from utils.metadata_extraction import extract_metadata
from utils.llm_integration import summarize_text, answer_query

# Set up the title of the app
st.title('Conversational Insights Platform')

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an audio/video file", type=['mp3', 'mp4', 'wav'])

# Define the directory where you want to save the uploaded files
UPLOAD_DIRECTORY = 'data/uploads'
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# Check if a file has been uploaded
if uploaded_file is not None:
    # Create a file path to save the uploaded file
    file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file.name)
    
    # Save the file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f'File uploaded and saved to {file_path}')
    
    # Transcription
    try:
        transcription = transcribe_audio(file_path)
        st.write("Transcription:")
        st.write(transcription)
    except Exception as e:
        st.error(f"Error in transcription: {e}")
    
    # Topic Extraction
    try:
        topics = extract_topics(transcription)
        st.write("Extracted Topics:")
        st.write(topics)
    except Exception as e:
        st.error(f"Error in topic extraction: {e}")
    
    # Sentiment Analysis
    try:
        sentiment = analyze_sentiment(transcription)
        st.write("Sentiment Analysis:")
        st.write(sentiment)
    except Exception as e:
        st.error(f"Error in sentiment analysis: {e}")
    
    # Metadata Extraction
    try:
        metadata = extract_metadata(file_path)
        st.write("Metadata:")
        st.write(metadata)
    except Exception as e:
        st.error(f"Error in metadata extraction: {e}")
    
    # Summarization
    try:
        with st.spinner('Generating summary...'):
            summary = summarize_text(transcription)
            st.write("Summary:")
            st.write(summary)
    except Exception as e:
        st.error(f"Error in summarization: {e}")
    
    # Query Answering
    query = st.text_input("Ask a question about the conversation:")
    if query:
        try:
            with st.spinner('Generating answer...'):
                answer = answer_query(query, transcription)
                st.write("Answer:")
                st.write(answer)
        except Exception as e:
            st.error(f"Error in query answering: {e}")
