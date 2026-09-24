import whisper
import json
import os

model = whisper.load_model("small")

# jsons folder agar nahi hai to bana dov
os.makedirs("jsons", exist_ok=True)

audios = os.listdir("audios")

for audio in audios:

    if "_" not in audio:
        continue

    print(audio)

    number = audio.split("_")[0]
    title = os.path.splitext(audio.split("_", 1)[1])[0]

    print(number, title)

    result = model.transcribe(
        audio=f"audios/{audio}",
        language="hi",
        task="translate",
        fp16=False,
        word_timestamps=False
    )

    segments = result["segments"]
    merged_chunks = []

    # Har 5 segments ko merge karo
    for i in range(0, len(segments), 5):
        group = segments[i:i+5]

        merged_chunks.append({
            "number": number,
            "title": title,
            "start": group[0]["start"],
            "end": group[-1]["end"],
            "text": " ".join(segment["text"].strip() for segment in group)
        })

    chunks_with_metadata = {
        "chunks": merged_chunks,
        "text": result["text"]
    }

    filename = os.path.splitext(audio)[0]

    with open(f"jsons/{filename}.json", "w", encoding="utf-8") as f:
        json.dump(chunks_with_metadata, f, ensure_ascii=False, indent=4)

    print(f"✅ Saved: jsons/{filename}.json")

print("🎉 All files completed.")
