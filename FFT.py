# FFT Definition

def Fourier(subjects): # I: subject * time * ROI
    subject_fft = []
    for timeset in subjects:
        np.transpose(timeset)
        x = [0 for i in range(len(timeset))]
        for ROI in range(len(timeset)):
            ROItimeset = timeset[ROI]
            N = len(timeset)
            for i in range(N-1):
                for x_i in ROItimeset:
                    x[ROI] += x_i*np.exp(2*np.pi*i/N)
        subject_fft.append(x)
    return subject_fft
