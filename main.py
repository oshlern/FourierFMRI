import numpy as np

w, h, l = 100, 100, 100

voxel_data = []
ROI_data = []

for _ in range(32):
    T = 500 + np.random.randint(500)
    voxels = np.random.rand(w, h, l, T)
    voxel_data.append(voxels)
    ROI = voxels[:,0,0,:]
    ROI_data.append(ROI)

# takes in vector of values through time
# returns vector amplitudes through frequencies

def fourier(data):
    # O: {freq: z}
    # |z| = amplitude of wave np.abs()
    # angle(z) = phase shift np.angle()

    F = {} # FOURIER RESULT

    #waves = [(amp, freq) for amp, freq in zip(sorted_amps, sorted_freqs)[:5]]
    wave = [(amp, freq, shift) for amp, freq, shift in map(F, lambda data: (np.abs(data[1]) data[0], np.angle(data[1])))]
    return

ROI_freqs = [fourier(ROI) for ROI in ROI_data]
