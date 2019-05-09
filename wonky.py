import numpy as np

def analyze(data):
    maxima = []
    t_since_last = 0
    last = ['peak', 0, 0]
    for x in data:
        if last[0] == 'peak':
            if x >= last[1]:
                last[1] = x
                last[2] += 1
            if x < last[1]:
                maxima.append(last)
                last = ['trough', x, 1]
        elif last[0] == 'trough':
            if x <= last[1]:
                last[1] = x
                last[2] += 1
            if x > last[1]:
                maxima.append(last)
                last = ['peak', x, 1]
    maxima.append(last)
    return maxima


n = 24
t = np.arange(n)

period = 4
phase = 0
sin = np.sin(t * (2*np.pi/period) + phase)

period2 = 3
phase2 = 1
sin2 = np.sin(t * (2*np.pi/period2) + phase2)
print(sin2)
print(sin)
print(sin+sin2)
print(analyze(sin+sin2))


# (amplitude, phase since last maxima)
