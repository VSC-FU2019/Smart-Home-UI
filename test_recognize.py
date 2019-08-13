import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
from keras.models import load_model
from python_speech_features import mfcc, logfbank, delta
from pydub import AudioSegment
import pyaudio
import IPython
from keras.preprocessing.sequence import pad_sequences
import scipy
import scipy.signal
import sys
import wave
from queue import Queue
from threading import Thread

NUMB_CEP = 13
NFFT = 512
DELTA = 2
MFCC_LEN = 200

model = load_model("./train-13.h5")

def get_feature(y, fs):
    y = y / np.max(abs((y)))
    mfcc_feat = mfcc(y, fs, numcep=NUMB_CEP)
    mfcc_feat = delta(mfcc_feat, DELTA)
                    
    return mfcc_feat

def preprocess_data(y, fs):
    b = scipy.signal.firwin(255, [300, 3400], pass_zero=False, fs=fs)
    y_filter = scipy.signal.filtfilt(b, 1, y)
    return y_filter
                                    
def get_data(y, fs):
    input_data = []
    mfcc_feat = get_feature(y, fs) 
    input_data.append(mfcc_feat)

    input_data[0] = pad_sequences(input_data[0].T, MFCC_LEN, dtype=float, padding='post', truncating='post').T
    input_data = np.array([input_data[0]])
    return input_data

def print_command(probabilities):
    arg_max = np.argmax(probabilities[0])
    if probabilities[0, arg_max] >= 0.75:
        if arg_max == 0:
            print("Background")
        elif arg_max == 1:
            print("Bat den")
        elif arg_max == 2:
            print("Tat den")
        elif arg_max == 3:
            print("Bat dieu hoa")
        elif arg_max == 4:
            print("Tat dieu hoa")
        elif arg_max == 5:
            print("Bat quat")
        elif arg_max == 6:
            print("Tat quat")
        elif arg_max == 7:
	    print("Bat tivi")
	elif arg_max == 8:
	    print("Tat tivi")
	elif arg_max == 9:
	    print("Mo cua")
	elif arg_max == 10:
	    print("Dong cua")
	elif arg_max == 11:
	    print("Khoa cua")
	elif arg_max == 12:
	    print("Mo cong")
	elif arg_max == 13:
	    print("Dong cong")
	elif arg_max == 14:
	    print("Khoa cong")
	elif arg_max == 15:
	    print("Doremon")
    else:
	sys.stdout.write("-")

## code detect
x = get_data(y, RATE)
prob = model.predict(x)
print_command(prob)
