import numpy as np
import matplotlib.pyplot as plt

def lowPass(data:np.ndarray, wc:float, *n:int):
    if not n:
        n=int(2*3.14159253593/wc)
    lit = np.sinc(2*wc*np.linspace(-n,n,2*n+1))
    lit /= np.sum(lit)
    return np.convolve(data,lit,"same")

def highPass(data:np.ndarray, wc:float, *n:int):
    if not n:
        n=int(2*3.14159253593/wc)
    lit = np.sinc(2*wc*np.linspace(-n,n,2*n+1))
    lit /= np.sum(lit)
    lit = 1.0*(np.arange(2*n+1)==n)-lit
    return np.convolve(data,lit,"same")

def stopBand(data:np.ndarray, wcb:float, wce:float, *n:int):
    if not n:
        n=int(2*3.14159253593/wcb)
    litl = np.sinc(2*wcb*np.linspace(-n,n,2*n+1))
    litl /= np.sum(litl)
    lith = np.sinc(2*wce*np.linspace(-n,n,2*n+1))
    lith /= np.sum(lith)
    lith = 1.0*(np.arange(2*n+1)==n)-lith
    lit = lith+litl
    lit /= np.sum(lit)
    return np.convolve(data,lit,"same")

def bandPass(data:np.ndarray, wcb:float, wce:float, *n:int):
    if not n:
        n=int(2*3.14159253593/wcb)
    litl = np.sinc(2*wcb*np.linspace(-n,n,2*n+1))
    litl /= np.sum(litl)
    lith = np.sinc(2*wce*np.linspace(-n,n,2*n+1))
    lith /= np.sum(lith)
    lith = 1.0*(np.arange(2*n+1)==n)-lith
    lit = lith+litl
    lit /= np.sum(lit)
    lit = 1.0*(np.arange(2*n+1)==n)-lit
    return np.convolve(data,lit,"same")

def main():
    fs = 44100.0
    fsin = 50.0
    duree = 1/fsin
    t = np.linspace(0,duree,int(duree*fs))
    data = np.random.normal(0,1,t.size)
    fdata = highPass(data,10000/44100)
    fig, ax1 = plt.subplots()
    ax1.plot(data)
    ax1.plot(fdata)
    qtebins = 21
    sp = np.fft.fft(data)
    fsp = np.fft.fft(fdata)
    freq = np.fft.fftfreq(data.shape[-1])
    ffreq = np.fft.fftfreq(fdata.shape[-1])
    fig, ax2 = plt.subplots()
    ax2.plot(freq*fs,np.absolute(sp))
    ax2.plot(ffreq*fs,np.absolute(fsp))
    plt.show()

if __name__ == "__main__":
    main()