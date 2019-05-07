# FFT Function
import numpy as np

def Discrete(subjects): # I: [subject * [time * [ROI]]]
    subject_fft = []
    for subject in subjects:
        np.transpose(subject) # Convert to [ROI * [timeset]]
        ListFreqROI = []
        for ROI in subject:
            N = len(ROI)
            X = [0 for k in range(N-1)]
            for k in range(N-1):
                for n in range(N-1):
                    X[n] += ROI[n] * np.exp(2*np.pi*k*n/N)
            ListFreqROI.append(X)
        subject_fft.append(ListFreqROI)
    return subject_fft

