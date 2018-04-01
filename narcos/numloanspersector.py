import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import pandas as pd

from narcos.kiva_data import KivaData
df = KivaData(use_sample=True).loan_data
df.describe()

def numloanssector():

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')
    #df.head()

    ts_df = df.groupby(['Qtr', 'sector'])['id'].count().reset_index()
    ts_df = ts_df[ts_df['Qtr'] < pd.Period('2017Q3')]
    # funded_amount
    plt.figure(figsize=(20, 10))
    sns.pointplot(
        x='Qtr',
        y='id',
        hue='sector',
        alpha=0.8,
        data=ts_df,
        palette="Set2")
    plt.title('Number of loans per Sector Over Time')
    plt.ylabel('Number of Loans')
    plt.xlabel('Quarter')

    plt.show()
