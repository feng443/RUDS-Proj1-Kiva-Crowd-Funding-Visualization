import matplotlib.pyplot as plt
import os
import pandas as pd

def number_loans_per_quarter(df):

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')
    df.head()

    numloanq = df.groupby(['Qtr'])['id'].count().reset_index()
    numloanq = numloanq[numloanq['Qtr'] < pd.Period('2017Q3')]
    #numloanq

    numloanq.plot.line(x='Qtr', y='id', figsize=(20, 4), marker='o')
    plt.title('Number of Loans Per Quarter')
    plt.ylabel("Number of Loans")
    plt.xlabel("Quarter")
    plt.savefig(os.path.join('image', 'number_loans_per_quarter_line.png'))
    plt.show()

    numloanq.plot.bar(x='Qtr', y='id', figsize=(20, 4))
    plt.title('Number of Loans Per Quarter')
    plt.ylabel("Number of Loans")
    plt.xlabel("Quarter")
    plt.savefig(os.path.join('image', 'number_loans_per_quarter_bar.png'))
    plt.show()




