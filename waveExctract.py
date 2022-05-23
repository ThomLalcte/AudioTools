import numpy as np
import wave as w

def wavExtract(file:str):
    audio = w.open(file,"rb")
    qteSamples = audio.getnframes()
    qteChannels = audio.getnchannels()
    data = np.zeros((qteChannels,qteSamples))
    if qteChannels == 2:
        for i in range(qteSamples):
            frame:bytes=audio.readframes(1)
            data[0][i] = int.from_bytes(frame[:2],"little",signed=True)
            data[1][i] = int.from_bytes(frame[-2:],"little",signed=True)
    if qteChannels == 1:
        for i in range(qteSamples):
            data[0][i] = int.from_bytes(audio.readframes(1),"little",signed=True)
    return data