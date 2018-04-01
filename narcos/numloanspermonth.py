import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import pandas as pd

def numloansmonth(df):

    df['date'] = pd.to_datetime(df['date'])
    df['year'], df['month'] = df['date'].dt.year, df['date'].dt.month
    #df

    df['mnth_yr'] = df['date'].apply(lambda x: x.strftime('%B-%Y'))
    #df.head()

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    #df.head()

    df.sort_values(by='date', inplace = True)
    #df.head()

    #Number of loans per month.
    df.groupby('mnth_yr2').agg('count')[['id']].plot.line(y='id', figsize=(20,10))
    plt.title('Number of Loans per Month')
    plt.ylabel("Number of Loans")
    plt.xlabel("MonthYear")
    plt.savefig('loanspermonth.png')
    #df.plot(figsize=(20,4))

    plt.show()