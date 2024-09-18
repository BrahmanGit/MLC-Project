from google.colab import drive
drive.mount('/content/drive')

import os
data_path = '/content/drive/MyDrive/MLC/firing_rates_Cori-14.npz'
large_data = np.load(data_path)
