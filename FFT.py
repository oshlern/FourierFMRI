# FFT Function
import numpy as np


def fft(data): # given list of values find dft
    N = len(data)

    if N == 1:
        # print(data)
        return data

    if N % 2 == 0:
        N2 = int(N/2)
        extra_term = False
    else:
        N2 = int((N-1)/2)
        extra_term = True

    # print(N, N2, extra_term)

    even_data = [data[2*i] for i in range(N2)]
    odd_data = [data[2*i+1] for i in range(N2)]

    even_freqs = fft(even_data)
    odd_freqs = fft(odd_data)
    print("--------------")

    freqs = [0]*(2*N2)
    for freq in range(N2):
        w = np.exp(-1j*np.pi/N2*freq)
        freqs[freq] = even_freqs[freq] + w * odd_freqs[freq]
        freqs[freq + N2] = even_freqs[freq] - w * odd_freqs[freq]
        # freqs[freq] = np.add(even_freqs, np.multiply(w, odd_freqs))
        # freqs[freq + N2] = np.subtract(even_freqs, np.multiply(w, odd_freqs))

    # extra_term = False

    if extra_term:
        # N-1 is the freq, which is 2*N2 so the inner powers cancel to 1 and is thus a sum
        # freqs.append(sum(even_data) + np.exp(-1j*2*np.pi/N*(N-1)) * sum(odd_data))
        # freqs.append()

        for freq in range(N-1):
            print(round(freqs[freq], 3))
            freqs[freq] = freqs[freq] + data[N-1]*np.exp(-1j*2*np.pi*(N-1)/N*freq)
            print(round(data[N-1]*np.exp(-1j*2*np.pi*(N-1)/N*freq), 3))
            print(round(freqs[freq], 3))
            print(freq)

        last_freq = sum([data[i] * np.exp(-1j*2*np.pi*i/N*(N-1)) for i in range(N)])
        print(last_freq, np.exp(-1j*2*np.pi/N*(N-1)))
        freqs.append(last_freq)

    return freqs

def dft(data):
    N = len(data)
    freqs = []
    for k in range(N):
        x = sum([data[i] * np.exp(-1j*2*np.pi*i/N*k) for i in range(N)])
        freqs.append(x)
    return freqs

def convert(freqs, d=2):
    new = []
    perc = 10 ** d
    for i in range(len(freqs)):
        mag, phase = np.abs(freqs[i]), np.angle(freqs[i])
        if mag > 0.002:
            print(i, mag, phase)
        new.append((i, (int(mag*perc)/perc), int(phase*perc)/perc))
    return new

def inverse_DFT(freqs):
    time_data = []
    N = len(freqs)
    for i in range(N):
        x = sum([freqs[j] * np.exp(1j*2*np.pi*j/N*i) for j in range(N)])
        time_data.append(x/N)
    return time_data



# freq is the number of cycles in the whole data set (0 = constant, N/2 = oscilate every other data-point)

n = 17

period = 8
phase = 1
t = np.arange(n)
sin = np.sin(t * (2*np.pi/period) + phase)

print(t)
print(sin)


freqs = fft(sin)
inv = np.real(inverse_DFT(freqs))

freqs2 = dft(sin)
inv2 = np.real(inverse_DFT(freqs2))

true_freqs = np.fft.fft(sin)
true_inv = np.real(inverse_DFT(true_freqs))
# print(convert(freqs))

print(inv)
print(inv2)

for i in range(len(freqs)):
    print(i, round(freqs[i],4), round(freqs2[i],4))#, round(true_freqs[i],4))
# print(freqs2)

# for ind, (s,i,i2) in enumerate(zip(sin, inv, inv2)):
#     if np.abs(s-i) > 0.03:
#         print(ind, s, i)
#     if np.abs(s-i2) > 0.03:
#         print("_", ind, s, i2)
# convert(fft(sin))
# print(convert(fft(sin)))
