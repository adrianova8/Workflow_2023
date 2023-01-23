# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

basket = pd.read_csv('/Users/adrianova/Desktop/Masters Data Science Santander/Máster Data Science UC/Asignaturas/Data Life Cycling /11. Workflows/players_stats.csv')

n_bins = 20

# Generate two normal distributions
dist1 = basket['Height']

# We can set the number of bins with the *bins* keyword argument.
plt.hist(dist1, bins=n_bins)
plt.title("Basketball height players")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.show()