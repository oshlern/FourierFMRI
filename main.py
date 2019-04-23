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
    return

ROI_freqs = [fourier(ROI) for ROI in ROI_data]
