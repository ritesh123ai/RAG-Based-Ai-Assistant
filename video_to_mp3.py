#convert the videos to mp3
import os
import subprocess
import os

files = os.listdir("videos")

for file in files:
    tutorial_number = file.split(" - ")[0]

    file_name = os.path.splitext(file)[0]

    # Number remove karo
    file_name = file_name.split(" - ", 1)[1]

    # Agar "｜" hai to uske pehle wala part lo
    file_name = file_name.split(" ｜ ")[0]

    # # Agar "：" hai to usko bhi remove kar do
    # file_name = file_name.split("：")[-1].strip()

    print(f"{tutorial_number} - {file_name}")
    subprocess.run(["ffmpeg", "-i",f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
