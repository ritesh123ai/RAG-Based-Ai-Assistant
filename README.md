# how to use this RAG AI Teaching assistant on your own data
## Step 1 -Collect your videos
Move all your video files to the videos folder

## Step 2- Convert to mp3
Convert all video files to mp3 by running video_to_mp3

## Step 3 - Convert mp3 to json
Convert all the mp3 files to json by running mp3_to_json

## Step 4 - Convert the json files to victor
Use the files preprocess_json to convert the json files to a dataframe with Embedding

## Step 5- Prompt generation and feeding to LLM

Read the joblib file and load it into the memory.Then create a relevant prompt  as per the user query and feed it to the LLM
