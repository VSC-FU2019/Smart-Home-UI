import pyaudio
import wave
 
FORMAT = pyaudio.paInt16 
CHANNELS = 1
RATE = 44100
CHUNK = 22050
WAVE_OUTPUT_FILENAME = "3.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("recording...")
frames = []
 
run = True 
seconds_rec_numb = 10    ## recording in 1 second
    
try:
    for i in range(0, int(seconds_rec_numb * RATE / CHUNK)):
        data = stream.read(CHUNK)
        frames.append(data)
except (KeyboardInterrupt, SystemExit):
    stream.stop_stream()
    stream.close()
    run = False

print("finished recording")
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
