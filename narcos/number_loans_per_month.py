import matplotlib.pyplot as plt
import os
import pandas as pd

def number_loans_per_month(df):

    df['date'] = pd.to_datetime(df['date'])
    df['year'], df['month'] = df['date'].dt.year, df['date'].dt.month

    df['mnth_yr'] = df['date'].apply(lambda x: x.strftime('%B-%Y'))

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))

    df.sort_values(by='date', inplace = True)

    #Number of loans per month.
    df.groupby('mnth_yr2').agg('count')[['id']].plot.line(y='id', figsize=(20,10), marker = 'o')
    plt.title('Number of Loans per Month')
    plt.ylabel("Number of Loans")
    plt.xlabel("MonthYear")
    plt.savefig(os.path.join('image', 'number_loans_per_month.png'))
    plt.show()
