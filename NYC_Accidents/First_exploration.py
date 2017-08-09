# First exploation of NYC Taxi acciendt data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from math import isnan
# asd


__author__ = "Sam Maddrell-Mander"
__copyright__ = "University of Bristol, August 2017"

def plot_scatter(data, var1, var2, filename_list=[''], cols='magma'):
    # data.plot(x=var1, y=var2)
    # plt.show()
    print("Plotting scatter plot...")
    x = data[var1][0:25000]
    y = data[var2][0:25000]
    xy = np.vstack([x, y])
    z = gaussian_kde(xy)(xy)
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]
    plt.scatter(x, y, c=z, s=2, edgecolor='', alpha=0.7, cmap=cols)
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.colorbar()
    plt.title(filename_list[0])
    plt.show()


def main():
    print("Loading the dataset")
    df = pd.read_csv("accidents_2016.csv", usecols=['LATITUDE', 'LONGITUDE', 'NUMBER OF PERSONS INJURED'])
    print(df.columns.values)
    df = df.loc[lambda df: df.LONGITUDE > -100]
    df_inj = df.loc[lambda df: df['NUMBER OF PERSONS INJURED'] > 0]
    df_fine = df.loc[lambda df: df['NUMBER OF PERSONS INJURED'] == 0]


    print("Number of rows:", len(df))
    df = df.dropna()
    print("Number of rows:", len(df))

    print(df.head())
    plot_scatter(df, 'LATITUDE', 'LONGITUDE')
    plt.scatter(df['LATITUDE'], df['LONGITUDE'], c=df['NUMBER OF PERSONS INJURED'],edgecolor='',s=2,alpha=0.7,)
    plt.show()

    plot_scatter(df_inj, 'LATITUDE', 'LONGITUDE')
    plot_scatter(df_fine, 'LATITUDE', 'LONGITUDE')
    plt.show()

    pass


if __name__ == "__main__":
    main()
