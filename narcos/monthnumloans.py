import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import pandas as pd

from narcos.kiva_data import KivaData
df = KivaData(use_sample=True).loan_data
df.describe()

def numloansmonth():

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')
    df.head()


    numloanmth = df.groupby(['mnth_yr2'])['id'].count().reset_index()
    #numloanq = numloanq[numloanq['Qtr'] < pd.Period('2017Q3')]
    numloanmth

    numloanmth.plot.line(x='mnth_yr2', y='id', figsize=(20, 4), marker='o')
    plt.title('Number of Loans Per Month')
    plt.ylabel("Number of Loans")
    plt.xlabel("Month")
    plt.show()

    numloanmth.plot.bar(x='mnth_yr2', y='id', figsize=(20, 4))
    plt.title('Number of Loans Per Month')
    plt.ylabel("Number of Loans")
    plt.xlabel("Month")
    plt.show()

    plt.show()


