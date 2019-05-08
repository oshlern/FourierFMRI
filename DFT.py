# DFT Function
import numpy as np
import matplotlib.pyplot as mpl

def Final(subjects): # I: [subject * [time * [ROI]]]
    subject_fft = []
    for subject in subjects:
        np.transpose(subject) # Convert to [ROI * [timeset]]
        ListFreqROI = []
        for ROI in subject:
            N = len(ROI)
            X = [0 for k in range(N-1)]
            for k in range(N-1):
                for n in range(N-1):
                    X[n] += ROI[n] * np.exp(2*np.pi*k*n*1j/N)
            ListFreqROI.append(X)
        subject_fft.append(ListFreqROI)
    return subject_fft

def convertToMagPhase(freqs, d=2):
    new = []
    perc = 10 ** d
    for i in range(len(freqs[0][0])):
        mag, phase = np.abs(freqs[0][0][i]), np.angle(freqs[0][0][i])
        if mag > 0.001:
            print(i, mag, phase)
        new.append((i, (int(mag*perc)/perc, int(phase*perc)/perc)))
    return new

def convertToSin(freqs):
    sin = np.sin(t * 0)
    for i in freqs:
        n = len(t)
        sin0 = i[1][0]*np.sin(t * (i[0]/(2*np.pi*n)) + i[1][0])
        sin = np.add(sin, sin0)
    sin = s[1][0]*np.sin(t * (s[0]/(2*np.pi*n)) + s[1][0])
    return sin

def convert(freqs): return convertToSin(convertToMagPhase(freqs))


n = 16

period = 8
phase = 0
t = np.arange(n)
sin = np.sin(t * (2*np.pi/period) + phase)

#print(t)
print(sin)
print(convert(Final([[sin]])))



## PLOT ##
#x = np.linspace(0, 10, 100)
dft_results = convert(Final([[sin]]))

# Plot the data
mpl.plot(t, sin, label='sin')
mpl.plot(t, dft_results, label="dft")

# Add a legend
mpl.legend()

# Show the plot
mpl.show()