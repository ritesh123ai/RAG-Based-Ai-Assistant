# RAG AI Teaching Assistant

## Overview

This project is a Retrieval Augmented Generation (RAG) based AI Teaching Assistant that allows users to interact with their own educational video data.

The system converts video lectures into searchable knowledge by extracting audio, generating transcripts, creating embeddings, and retrieving relevant information using semantic search.

## How to Use This RAG AI Teaching Assistant on Your Own Data

## Step 1: Collect Video Data

Collect all the required educational video files.

Store the videos inside the `videos/` directory.

---

## Step 2: Convert Video to Audio

Extract audio from all video files.

Run the `video_to_mp3.py` script to convert videos into MP3 format.

The generated audio files are stored in the `audios/` directory.

---

## Step 3: Convert Audio to JSON Transcripts

Convert MP3 audio files into structured JSON files using the `mp3_to_json.py` script.

Speech-to-text conversion is performed using Whisper to generate transcripts with timestamps.

The generated JSON files are stored in the `jsons/` directory.

---

## Step 4: Generate Embeddings

Process the JSON transcript files using `preprocess_json.py`.

Convert text chunks into vector embeddings using the bge-m3 embedding model.

The generated embeddings are stored and used for semantic search and retrieval.

---

## Step 5: Prompt Generation and LLM Response

Load the generated embedding file into memory.

When a user submits a query:

1. Convert the query into an embedding.
2. Perform similarity search to retrieve relevant context.
3. Generate a contextual prompt.
4. Send the prompt to the Large Language Model (LLM).
5. Return the final AI-generated response.

---

## Project Workflow

Video Files
↓
Audio Conversion using FFmpeg
↓
Speech-to-Text using Whisper
↓
JSON Transcript Generation
↓
Text Chunk Processing
↓
Embedding Generation using bge-m3
↓
Similarity Search
↓
Context Retrieval
↓
LLM Response Generation

---

## Tech Stack

- Python
- Whisper
- Ollama
- bge-m3 Embedding Model
- FFmpeg
- Vector Similarity Search
- NumPy
- Pandas
- Deepseek-r1
- Scikit-learn

---

## Features

- Converts educational videos into searchable knowledge.
- Generates transcripts with timestamps.
- Creates embeddings for semantic search.
- Retrieves relevant information from video content.
- Generates AI-based responses using retrieved context.

---

## Future Improvements

- Add web-based user interface.
- Support more data sources like PDFs and documents.
- Improve retrieval accuracy.
- Add conversation memory.
