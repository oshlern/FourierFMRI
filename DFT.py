# DFT Functions
import numpy as np
import numpy.fft as npf
import matplotlib.pyplot as mpl

# def Final(subjects): # I: [subject * [time * [ROI]]]
#     subject_fft = []
#     for subject in subjects:
#         np.transpose(subject) # Convert to [ROI * [timeset]]
#         ListFreqROI = []
#         for ROI in subject:
#             N = len(ROI)
#             X = [0 for k in range(N-1)]
#             for k in range(N-1):
#                 for n in range(N-1):
#                     X[n] += ROI[n] * np.exp(-2*np.pi*k*n*1j/N)
#             ListFreqROI.append(X)
#         subject_fft.append(ListFreqROI)
#     return subject_fft

def DFT(x, N=10): # x is the data, N is buckets... I wrote it like this to better mimic the standard DFT equation notation
    X = np.arange(N)*0
    for n in range(N):
        # Loop through to define each X_n 
        for k in range(len(x)): # k is a discrete timestep variable, data[k] is the data at this point
            # For some X_n, sum up the value for each time step k
            X[n] += x[k] * np.exp(-1j*2*np.pi*k*n/N) # \sum_{k=0}^{M-1} x_k^{-i\frac{2pi}{N}\cdot kn} where M is the length of the signal
    return X

def convertToMagPhase(freqs, d=2):
    new = []
    perc = 10 ** d
    for i in range(len(freqs)):
        mag, phase = np.abs(freqs[i]), np.angle(freqs[i])
        if mag > 0.001:
            pass#print(i, mag, phase)
        new.append((i, (int(mag*perc)/perc, int(phase*perc)/perc)))
    return new

def convertToSin(freqs):
    sin = np.sin(0)
    for i in freqs:
        n = len(t)
        sin0 = i[1][0]*np.sin(t * (i[0]/(2*np.pi*n)) + i[1][0])
        sin = np.add(sin, sin0)
    return sin

def convert(freqs): return convertToSin(convertToMagPhase(freqs))


n = 16
t = np.arange(n)

period = 8
phase = 0
sin = np.sin(t * (2*np.pi/period) + phase)

#print(t)
#print(sin)
#print("\"", DFT([[sin]]), "\"")
for i in DFT(sin):
    print(np.abs(i))


## PLOT ##
#x = np.linspace(0, 10, 100)
dft_results = convert(DFT(sin))

# Plot the data
mpl.plot(t, sin, label='sin')
mpl.plot(t, dft_results, label="dft")
mpl.plot(t, convert(npf.fft(sin)), label="np.fft")

# Add a legend
mpl.legend()

# Show the plot
mpl.show()
