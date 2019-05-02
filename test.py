import numpy as np
complex_data = np.exp(2j * np.pi * np.arange(8))
period = 4
t = np.arange(16)/period*2*np.pi
sin = np.sin(t + np.pi)
print(t)
print(sin)
fft = np.fft.fft(sin)
print(fft)

# # FFT Definition

# import numpy as np

# def Fourier(subjects): # I: subject * time * ROI
#     subjects_fft = []
#     for subject in subjects:
#         ts, ROIs = np.shape(subject)
#         x = np.zeros(ROIs)

#         for ROI in range(len(timeset)):
#             ROItimeset = timeset[ROI]
#             N = len(timeset)
#             for i in range(N-1):
#                 for x_i in ROItimeset:
#                     x[ROI] += x_i*np.exp(2*np.pi*i/N)
#         subject_fft.append(x)
#     return subject_fft

# # np.fft(subjects, axis=1)