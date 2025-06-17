import pvporcupine
import pyaudio
import struct

wake_word_heard = False

def reset_listening_flag():
    global wake_word_heard
    wake_word_heard = False

def wait_for_wake_word_continuous(access_key, keyword_path):
    global wake_word_heard
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[keyword_path]
    )

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    try:
        while not wake_word_heard:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            result = porcupine.process(pcm)
            if result >= 0:
                wake_word_heard = True
                print("wakeup word triggered!")
                break
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()