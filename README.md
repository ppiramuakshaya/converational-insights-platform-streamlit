# Conversational Insights Platform

## Overview

The Conversational Insights Platform is a web application that processes audio and video files to transcribe content, extract topics, analyze speaker sentiments, and generate insights. It handles panel discussions in video format and customer-agent conversations in audio format, specifically within a retail context.

## Features

- **Data Ingestion:** Upload and process audio and video files.
- **Transcription:** Convert speech to text using Automatic Speech Recognition (ASR).
- **Topic Extraction:** Identify key topics from the transcribed text using NLP techniques.
- **Metadata Extraction:** Extract and display metadata from the media files.
- **Sentiment Analysis:** Analyze the sentiment of speaker statements.
- **Insight Generation:** Generate actionable insights based on transcriptions and analyses.
- **User Interface:** Interactive web dashboard built with Streamlit.
- **Integration with LLM:** Use a Large Language Model to summarize and answer queries about the conversation.

## Prerequisites

- Python 3.x
- `ffmpeg`
- A GitHub account (for version control and collaboration)

## Installation

 **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/conversational-insights-platform.git
   cd conversational-insights-platform
## Set Up a Virtual Environment:

**Create a Virtual Environment:**

Run the following command to create a virtual environment:


python -m venv venv


## Activate a virtual environment
Run the following command

venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

Streamlit is used for user interface.
