import pyaudio
import wave
import speech_recognition as sr
from os import path
import threading
import sys

HELPER_PATH = path.dirname(path.realpath(__file__)) + "/Identification"
sys.path.insert(0, HELPER_PATH)
import IdentificationServiceHttpClientHelper

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), WAVE_OUTPUT_FILENAME)


def content():
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        sys.stderr.write("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        sys.stderr.write("Could not request results from Google Speech Recognition service; {0}".format(e))

    sys.stdout.flush()


def speaker():
    "ok"

    #path = "output.wav"

    profile_ids = ["7236a4fe-11f4-42c0-b2f5-2296675bbd11", "10e63fa3-4fd0-4449-b89d-97d12ba5f6de",
                   "ca5e9df5-eb2c-4e14-9172-552a01078c52", "afd6ae1d-52d4-4d35-a476-d9d11559a853",
                   "bb038c6c-d34a-4851-b19c-7770a09615c2"]

    subscription_key = '172ed99890704259b5e86a561129f3eb'
    force_short_audio = 'true'
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(subscription_key)

    identification_response = helper.identify_file(
        AUDIO_FILE, profile_ids,
        force_short_audio.lower() == "true")
    try:
        if (identification_response.get_identified_profile_id() == "7236a4fe-11f4-42c0-b2f5-2296675bbd11"):
            print('user:Frank')
        elif (identification_response.get_identified_profile_id() == "10e63fa3-4fd0-4449-b89d-97d12ba5f6de"):
            print('user:Dhanesh')
        elif (identification_response.get_identified_profile_id() == "ca5e9df5-eb2c-4e14-9172-552a01078c52"):
            print('user:Deagan')
        elif (identification_response.get_identified_profile_id() == "afd6ae1d-52d4-4d35-a476-d9d11559a853"):
            print('user:Yidan')
        elif (identification_response.get_identified_profile_id() == "bb038c6c-d34a-4851-b19c-7770a09615c2"):
            print('user:Isaac')
        else:
            sys.stderr.write('Cannot Identify Speaker')

    except:
        sys.stderr.write('Error Return')

    sys.stdout.flush()


threads = []
frames = []
s = 0
while True:
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("* recording")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    if (len(frames) > 150):
        frames = frames[75:225]

    #print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(AUDIO_FILE, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    t = threading.Thread(target = content)
    threads.append(t)
    t.start()

    if (s == 1) :
        t = threading.Thread(target = speaker)
        threads.append(t)
        t.start()
        s = 0
    else:
        s = 1
