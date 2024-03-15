from gtts import gTTS
import os
data_text = ""
audio = gTTS(text=data_text, lang="ru", slow=False)
audio.save("voice.mp3")
os.system("start voice.mp3")