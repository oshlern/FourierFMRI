# FFT Definition

def Fourier(subjects): # I: subject * time * ROI
    for timeset in subjects:
        np.transpose(timeset)

        x = [0 for i in range(len(timeset))]
        for ROI in range(len(timeset)):
            ROItimeset = timeset[ROI]
            N = len(timeset)
            for i in range(N-1)
                x[ROI] += x_i*np.exp(2*np.pi*i/N) #x_n*e^(-i2pikn/N)

            