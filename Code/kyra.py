import os
import sys
import time
import threading
import queue
import requests
import speech_recognition as sr
import pyttsx3
from functions.wakeup import wait_for_wake_word_continuous, reset_listening_flag

# api keys
GROQ_KEY = ""
PV_ACCESS_KEY = ""
WAKEWORD_MODEL = r"models\hey-kyra_en_windows_v3_0_0.ppn"

# TTS setup
speech_queue = queue.Queue()
stop_speaking = threading.Event()
is_speaking = threading.Event()

def tts_worker():
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)

    voices = engine.getProperty('voices')
    if len(voices) > 2:
        engine.setProperty('voice', voices[2].id)

    while True:
        text = speech_queue.get()
        if text is None:
            break

        if stop_speaking.is_set():
            print("[INFO] speech interrupted.")
            with speech_queue.mutex:
                speech_queue.queue.clear()
            stop_speaking.clear()
            continue

        try:
            is_speaking.set()
            engine.say(text)
            engine.runAndWait()
            is_speaking.clear()
        except Exception as e:
            print(f"[ERROR] TTS engine crashed: {e}")
            is_speaking.clear()
            engine = pyttsx3.init()
            engine.setProperty("rate", 180)
            if len(voices) > 2:
                engine.setProperty('voice', voices[2].id)

tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def speak(text):
    stop_speaking.clear()
    speech_queue.put(text)

# groq api
def ask_groq(prompt):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistral-saba-24b",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[ERROR] failed to get response from groq: {e}")
        return "sorry, I ran into a problem while trying to answer that."

# voice listen
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("[INFO] listening for your command.")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"[YOU] {query}")
        return query
    except sr.UnknownValueError:
        print("[ERROR] couldn't understand audio.")
        return ""
    except sr.RequestError:
        print("[ERROR] issue with recognition service.")
        return ""

# main looop
if __name__ == "__main__":
    print("[INFO] Kyra assistant is now running.")
    while True:
        reset_listening_flag()
        print("[INFO] waiting for 'Hey Kyra'")

        wait_for_wake_word_continuous(PV_ACCESS_KEY, WAKEWORD_MODEL)

        if is_speaking.is_set():
            print("[INFO] interrupting current response.")
            stop_speaking.set()
            time.sleep(0.1)

        query = listen()
        if query:
            print("[INFO] sending query to groq")
            response = ask_groq(query)
            print(f"[KYRA] {response}\n")
            speak(response)
        else:
            print("[INFO] no valid input received. restarting Kyra listen.\n")