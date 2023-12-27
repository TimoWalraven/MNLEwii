import numpy as np
from EntropyHub import SampEn
from pyentrp import entropy as ent
import timeit

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
fileName = 'testrecordings/Timo.xlsx'
try:
    import pandas as pd
    data = pd.read_excel(fileName, sheet_name='Data')
    data = data.to_numpy()
except Exception as e:
    print(f"Error while opening file: {e}")
    exit(1)

# get second and third column
data = data[:, 1]
std = np.std(data)

# time the function
#print(timeit.timeit(lambda: sample_entropy(data, 2, 0.2), number=10))
#print(timeit.timeit(lambda: SampEn(data, 2, 0.2), number=10))
print(timeit.timeit(lambda: ent.sample_entropy(data, 2, 0.2), number=10))
