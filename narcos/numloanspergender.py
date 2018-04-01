import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import pandas as pd

from narcos.kiva_data import KivaData
df = KivaData(use_sample=True).loan_data
df.describe()

def numloansgender():

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')
    #df.head()

    genderdf = df.groupby(['mnth_yr2', 'gender']).agg('count')[['id']]
    genderdf.head()


    gd_df = df.groupby(['Qtr', 'gender'])['id'].count().reset_index()
    gd_df = gd_df[gd_df['Qtr'] < pd.Period('2017Q3')]
    plt.figure(figsize=(20,10))
    sns.pointplot(
        x='Qtr',
        y='id',
        hue='gender',
        alpha = 0.8,
        data=gd_df)
    plt.title('Number of Loans per Gender Over Time')
    plt.ylabel('Number of Loans')
    plt.xlabel('Quarter')
    plt.show()
