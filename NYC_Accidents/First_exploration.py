# First exploation of NYC Taxi acciendt data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from math import isnan


__author__ = "Sam Maddrell-Mander"
__copyright__ = "University of Bristol, August 2017"

def plot_scatter(data, var1, var2, filename_list=['']):
    # data.plot(x=var1, y=var2)
    # plt.show()
    print("Plotting scatter plot...")
    x = data[var1][0:10000]
    y = data[var2][0:10000]
    xy = np.vstack([x, y])
    z = gaussian_kde(xy)(xy)
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]
    plt.scatter(x, y, c=z, s=2, edgecolor='', alpha=0.7)
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.colorbar()
    plt.title(filename_list[0])
    plt.show()


def main():
    print("Loading the dataset")
    df = pd.read_csv("accidents_2016.csv")
    print(df.columns.values)
    print("Number of rows:", len(df))
    df.dropna()
    print("Number of rows:", len(df))

    # df = df.loc[lambda df: (isnan(float(df.LATITUDE)) != True )]
    print(df['LATITUDE'])#, 'LONGITUDE'])
    plot_scatter(df, 'LATITUDE', 'LONGITUDE')

    pass


if __name__ == "__main__":
    main()
