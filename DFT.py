# DFT Functions
import numpy as np
import numpy.fft as npf
import matplotlib.pyplot as mpl
from random import randint

def add(list1, list2):
    if len(list1) != len(list2): raise IndexError("WTF")
    list3 = [0 for i in range(len(list1))]
    for i in range(len(list1)):
        list3[i] = list1[i] + list2[i]
    return list3

def DFT(x, N=10): # x is the data, N is buckets... I wrote it like this to better mimic the standard DFT equation notation
    X = np.arange(N)*0
    for n in range(N):
        # Loop through to define each X_n 
        for k in range(len(x)): # k is a discrete timestep variable, data[k] is the data at this point
            # For some X_n, sum up the value for each time step k
            X[n] += np.multiply(x[k], np.exp(-1j*2*np.pi*k*n/N)) # \sum_{k=0}^{M-1} x_k^{-i\frac{2pi}{N}\cdot kn} where M is the length of the signal
    return X

def convertToMagPhase(freqs, d=2):
    new = []
    perc = 10 ** d
    for i in range(len(freqs)):
        mag, phase = np.abs(freqs[i]), np.angle(freqs[i])
        if mag > 0.001:
            pass#print(i, mag, phase)
        new.append((i+1, int(mag*perc)/perc, int(phase*perc)/perc))
    return new # O: (freq, mag, arg)

def convertToSin(freqs, printval=False):
    t = np.arange(n)
    sin = np.sin(t * 0)
    for i in freqs:
        sin0 = np.multiply(i[1],np.sin(t * (i[0]*n/(2*np.pi)) + i[2]))
        sin = add(sin, sin0)
        if printval: print("~",sin)
    if printval: print("\"",freqs[0])
    return sin

def convert(freqs): return convertToSin(convertToMagPhase(freqs))


## PLOT ##
n = 16#randint(10,40)
print("n",n)
t = np.arange(n)

period = 8
phase = 0

sin1 = np.sin(t * (2*np.pi/period) + phase)
sin2 = np.sin(t * (2*np.pi/(2*period)) + phase)
sin3 = np.sin(t * (2*np.pi/(3*period)) + phase)
TestData = add(add(sin1, sin2), sin3)

# Print the data
dft_calc = DFT(TestData)
for i in range(len(dft_calc)):
    print("freq", i, "-- -- -- mag", np.abs(dft_calc[i]), "-- -- -- arg", np.angle(dft_calc[i]))

# Plot the data
# mpl.plot(t, TestData, label='sin')
mpl.plot(t, convert(dft_calc), label="dft")
mpl.plot(t, convert(npf.fft(TestData)), label="np.fft")

# for i in convertToMagPhase(dft_calc):
#     sin0 = np.multiply(i[1],np.sin(t * (n/(2*np.pi*i[0])) + i[2]))
#     if i[1] != 0: mpl.plot(t, sin0, label=("sin"+str(i)))

# Add a legend
mpl.legend()

# Show the plot
mpl.show()
