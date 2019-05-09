def DFT(x, N=10): # x is the signal, N is buckets... I wrote it like this to better mimic the standard DFT equation notation
    X = [0 for i in range(N)]
    for n in range(N):
        # Loop through to define each X_n 
        for k in range(len(x)): # k is a discrete timestep variable, data[k] is the data at this point
            # For some X_n, sum up the value for each time step k
            X[n] = np.add(X[n],np.multiply(x[k], np.exp(-1j*2*np.pi*k*n/N))) # \sum_{k=0}^{M-1} x_k^{-i\frac{2pi}{N}\cdot kn} where M is the length of the signal
    return X