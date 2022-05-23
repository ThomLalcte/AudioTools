#!/usr/bin/env python
import matplotlib.pyplot as plt
import waveExctract as we
import wave as w
import filters as f
import numpy as np

def processChunk(data:np.ndarray,fs:int,wcb:int,wce:int):
    sp = np.absolute(np.fft.fft(data))
    return np.sum(sp[wcb//fs:wce//fs])/np.sum(sp)


data = we.wavExtract("C:/Users/mimas/Desktop/castle.wav")
metadata = w.open("C:/Users/mimas/Desktop/castle.wav","rb")

size = data[0].size
chunksize = 1024
fs = metadata.getframerate()
freqContent = np.zeros((2,size//chunksize+1))
for chunk in range(size//chunksize+1):
    freqContent[0][chunk] = processChunk(data[0][chunk*chunksize,(chunk+1)*chunksize],fs,0,150)