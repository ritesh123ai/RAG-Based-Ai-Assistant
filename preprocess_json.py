import requests
import os
import json
import time
import pandas as pd
import joblib


# ==========================
# CONFIG
# ==========================
MODEL = "bge-m3"
BATCH_SIZE = 16
MAX_RETRIES = 5
TIMEOUT = 300


# ==========================
# EMBEDDING FUNCTION
# ==========================
def create_embedding(text_list):

    for attempt in range(MAX_RETRIES):

        try:

            r = requests.post(
                "http://localhost:11434/api/embed",
                json={
                    "model": MODEL,
                    "input": text_list
                },
                timeout=TIMEOUT
            )

            if r.status_code == 200:

                data = r.json()

                if "embeddings" in data:
                    return data["embeddings"]

                print("Unexpected Response:", data)

            else:

                print(f"\nStatus Code: {r.status_code}")
                print(r.text)

        except Exception as e:

            print(f"\nAttempt {attempt+1}/{MAX_RETRIES} Failed")
            print(e)

        if attempt != MAX_RETRIES - 1:

            print("Retrying in 5 seconds...\n")
            time.sleep(5)

    raise Exception("Embedding API failed after multiple retries")


# ==========================
# READ JSON FILES
# ==========================
jsons = sorted(os.listdir("jsons"))

my_dicts = []

chunk_id = 0


for json_file in jsons:

    with open(f"jsons/{json_file}", encoding="utf-8") as f:

        content = json.load(f)

    print(f"\n{'='*60}")
    print(f"Creating Embeddings for {json_file}")
    print(f"{'='*60}")

    texts = [c["text"] for c in content["chunks"]]

    embeddings = []

    # Batch Processing
    for start in range(0, len(texts), BATCH_SIZE):

        end = min(start + BATCH_SIZE, len(texts))

        print(f"Batch {start+1} - {end}")

        batch = texts[start:end]

        batch_embeddings = create_embedding(batch)

        embeddings.extend(batch_embeddings)

    # Save embeddings
    for i, chunk in enumerate(content["chunks"]):

        chunk["chunk_id"] = chunk_id

        chunk["embedding"] = embeddings[i]

        chunk_id += 1

        my_dicts.append(chunk)


print("\nCreating DataFrame...")

df = pd.DataFrame.from_records(my_dicts)

joblib.dump(df, "embeddings.joblib")

print("\n====================================")
print("✅ Embedding Creation Completed")
print("====================================")
print(f"Total Chunks : {len(df)}")
print("Saved File   : embeddings.joblib")
