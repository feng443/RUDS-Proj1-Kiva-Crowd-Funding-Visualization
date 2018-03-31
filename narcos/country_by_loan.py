#from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
#import requests
#import json
#import numpy as np
import os

def plot_country_by_loan_amount(df):
    country_df = df[['country', 'loan_amount']].groupby("country").sum()
    country_df['loan_ranked'] = df[['country', 'loan_amount']].groupby("country").sum().rank(ascending=True)
    country_df_filtered = country_df[country_df['loan_ranked'] < 5]
    # c = country_df.groupby("country").agg('sum')[['loan_amount']]/100000
    country_df_filtered.reset_index(inplace=True)
    print(country_df_filtered)

    country_df_filtered.plot.barh(x='country', y='loan_amount', color=['b', 'r', 'y', 'g', ], align='edge')
    plt.savefig(os.path.join('image', 'coutry_by_loan.png'))

    plt.show()
