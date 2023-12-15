import numpy as np
from EntropyHub._SampEn import SampEn
from pyentrp import entropy as ent

def sample_entropy(series, m, r):
    """
    Calculate the sample entropy of a given time series data without Numba optimization.

    :param series: list or numpy array of time series data
    :param m: length of sequences to be compared
    :param r: tolerance for accepting matches
    :return: sample entropy value
    """
    series = np.asarray(series)
    N = len(series)
    r *= np.std(series)

    def _count_matches(series, m, r):
        B = 0.0
        A = 0.0

        for i in range(N - m):
            template = series[i:(i + m)]

            for j in range(i + 1, N - m):
                if np.abs(series[j:(j + m)] - template).max() <= r:
                    B += 1
                    if np.abs(series[j + m] - series[i + m]) <= r:
                        A += 1

        return A, B

    A, B = _count_matches(series, m, r)

    # Avoid division by zero
    if B == 0:
        return float('inf')

    return -np.log(A / B)


# load np array from csv
data = np.genfromtxt('testrecordings/test 100hz  2.csv', delimiter=' ', skip_header=1)
data = data[:, 1]
std = np.std(data)
sample_entropy1 = sample_entropy(data, 2, 0.2)
sample_entropy2 = SampEn(data, 2, 1, 0.2*std)
sample_entropy3 = ent.sample_entropy(data, 2, 0.2*std)
print(f'{sample_entropy1:.3f}')
print(f'{sample_entropy2}')
print(f'{sample_entropy3}')

