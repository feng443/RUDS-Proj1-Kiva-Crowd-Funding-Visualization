from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
from narcos.kiva_data import KivaData
import requests
from narcos.fixer_config import access_key
import json
import numpy as np

from narcos.kiva_data import KivaData
from forex_python.converter import CurrencyRates
from functools import partial
import seaborn as sns

kiva_data = KivaData(use_sample=True)
df = kiva_data.loan_data

def plot_country_by_loan_amount():
    country_df = df[['country', 'loan_amount']].groupby("country").sum()
    country_df['loan_ranked'] = df[['country', 'loan_amount']].groupby("country").sum().rank(ascending=True)
    country_df_filtered = country_df[country_df['loan_ranked'] < 5]
    # c = country_df.groupby("country").agg('sum')[['loan_amount']]/100000
    country_df_filtered.reset_index(inplace=True)
    print(country_df_filtered)

    country_df_filtered.plot.barh(x='country', y='loan_amount', color=['b', 'r', 'y', 'g', ], align='edge')

    plt.show()
