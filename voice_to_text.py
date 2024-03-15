import speech_recognition as sr

def command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите хоть слово....")
        rec.pause_threshold = 1
        rec.adjust_for_ambient_noise(source, duration=1)
        data_audio = rec.listen(source)
    try:
        result = rec.recognize_google(data_audio, language="ru-RU").lower()
        print(f"Вы сказали: {result}")
    except sr.UnknownValueError:
        print("Не понимаю вас")
        result = command()
    return result


while True:
    command()

