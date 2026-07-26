# how to use this RAG AI Teaching assistant on your own data
## Step 1: Collect Video Data
Collect all the required educational video files.
Store the videos inside the videos/ directory

## Step 2: Convert Video to Audio
Extract audio from all video files.
Run the video_to_mp3.py script to convert videos into MP3 format.
The generated audio files are stored in the audios/ directory.

## Convert Audio to JSON Transcripts
Convert MP3 audio files into structured JSON files using the mp3_to_json.py script.
Speech-to-text conversion is performed to generate transcripts with timestamps.
The generated JSON files are stored in the jsons/ directory.

## Generate Embeddings
Process the JSON transcript files using preprocess_json.py.
Convert text chunks into vector embeddings using the embedding model.
Store embeddings for semantic search and retrieval.

## Prompt Generation and LLM Response
Load the generated embedding file into memory.
When a user submits a query:
Convert the query into an embedding.
Perform similarity search to retrieve relevant context.
Generate a contextual prompt.
Send the prompt to the Large Language Model (LLM).
Return the final AI-generated response.
