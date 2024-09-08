import os
import whisper
# my_secret = os.environ['OPENAI_API_KEY']



model = whisper.load_model("base")
result = model.transcribe("test2.mp3")
print(result["text"])
