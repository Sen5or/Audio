import pyaudio
import wave
import speech_recognition as sr
from os import path
import threading
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), WAVE_OUTPUT_FILENAME)




frames = []
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
				channels=CHANNELS,
				rate=RATE,
				input=True,
				frames_per_buffer=CHUNK)

print("* recording")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	data = stream.read(CHUNK)
	frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(AUDIO_FILE, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

