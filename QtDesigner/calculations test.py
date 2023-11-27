import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from code_descriptors_postural_control.stabilogram.stato import Stabilogram
from code_descriptors_postural_control.descriptors import compute_all_features


forceplate_file_selected = "dummyrec.csv"

data_forceplatform = pd.read_csv(forceplate_file_selected, sep=" ", index_col=0)
dft = data_forceplatform

# get first 2 columns
X = dft['x']
Y = dft['y']

X = X - np.mean(X)
Y = Y - np.mean(Y)

time = dft.index.to_numpy()
X = X.to_numpy()
Y = Y.to_numpy()


fig, ax = plt.subplots(1)
ax.plot(X)
ax.plot(Y)
fig.show()

data = np.array([time, X, Y]).T

# Verif if NaN data
valid_index = (np.sum(np.isnan(data), axis=1) == 0)

if np.sum(valid_index) != len(data):
    raise ValueError("Clean NaN values first")

stato = Stabilogram()
stato.from_array(array=data, resample_frequency=100)

print(stato.signal)

fig, ax = plt.subplots(1)
ax.plot(stato.medio_lateral)
ax.plot(stato.antero_posterior)
fig.show()

sway_density_radius = 0.3  # 3 mm

params_dic = {"sway_density_radius": sway_density_radius}

features = compute_all_features(stato, params_dic=params_dic)
print(features)

