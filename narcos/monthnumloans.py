import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import pandas as pd


def num_loans_month():

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')

    numloanmth = df.groupby(['mnth_yr2'])['id'].count().reset_index()

    fig, ax = plt.figure(figsize=(20,8))
    
    plt.subplot(211)
    numloanmth.plot.line(x='mnth_yr2', y='id', figsize=(20, 4), marker='o')
    plt.title('Number of Loans Per Month')
    plt.ylabel("Number of Loans")
    plt.xlabel("Month")
    
    plt.subplot(211)
    numloanmth.plot.bar(x='mnth_yr2', y='id', figsize=(20, 4))
    plt.title('Number of Loans Per Month')
    plt.ylabel("Number of Loans")
    plt.xlabel("Month")
    
    plt.show()