import pyttsx3
import easyocr
import keyboard
from capture import get_capture

def txt(img_path):
    reader = easyocr.Reader(["en"],model_storage_directory="models")
    result = reader.readtext(image=img_path,
                                detail=0,
                                paragraph=True)
    return result

def tts(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("volume", 0.7)#standard -> 1.0
    engine.setProperty("voice",voices[0].id)
    engine.say(text)
    engine.runAndWait()


def main():
    capture = get_capture()
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            if event.name == "s":
                capture()
                text = txt("images/screen.png")
                if text:
                    tts(" ".join(str(t) for t in text))
            elif event.name == "d":
                break

if __name__=="__main__":
    main()