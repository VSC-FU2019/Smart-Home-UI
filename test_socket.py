import socketio
from scipy.io import wavfile
import json
import pyaudio
import numpy as np

sio = socketio.Client()
server_ip = 'http://phanmduong.xyz:5000'
FORMAT = pyaudio.paInt16
NUMB_CHANNEL = 1
RATE = 8000
CHUNK = 2000
SECOND_RECORD = 2
SAMPLE_RECORD = int(RATE * SECOND_RECORD)

data = np.zeros(SAMPLE_RECORD, dtype='int16')

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
   print('disconnected from server')
    
#sio.connect(server_ip)

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=NUMB_CHANNEL, rate=RATE, input=True,frames_per_buffer=CHUNK)

run = True 
try:
    while run:
        data0 = stream.read(CHUNK)
        data = np.append(data, data0)
        if len(data) > SAMPLE_RECORD:
            data = data[-SAMPLE_RECORD:]
            ### send 2s data to server
            sio.emit("send data", json.dumps(data.tolist()))

except (KeyboardInterrupt, SystemExit):
    stream.stop_stream()
    stream.close()
    run = False

stream.stop_stream()
stream.close()
audio.terminate()
