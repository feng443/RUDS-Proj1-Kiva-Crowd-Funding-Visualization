
# coding: utf-8

# In[ ]:



import matplotlib.pyplot as plt
import os
import pandas as pd

def number_loans_per_quarter(df):

    figure = plt.figure(figsize=(14,8))
    
    ax1 = plt.subplot2grid((2, 1), (0, 0))
    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')

    numloanq = df.groupby(['Qtr'])['id'].count().reset_index()
    numloanq = numloanq[numloanq['Qtr'] < pd.Period('2017Q3')]
    #numloanq

    numloanq.plot.line(x='Qtr', y='id', marker='o', ax=ax1)
    #plt.title('Number of Loans Per Quarter')
    plt.title('Loans Per Quarter')
    plt.ylabel("Number of Loans")
    #plt.xlabel("Quarter")
    #plt.savefig(os.path.join('image', 'number_loans_per_quarter_line.png'))
    
    #Dataframe grouped by quarter. Takes the mediam loan amount per quarter.
    medloanq = df.groupby('Qtr').agg('median')[['loan_amount']]

    ax2 = plt.subplot2grid((2, 1), (1, 0))
    medloanq.plot.line(y='loan_amount',marker='o', ax=ax2)
    #plt.title('Median Loan Amount Per Quarter')
    plt.ylabel("Median Loan Amount")
    plt.xlabel("Quarter")
    #plt.savefig(os.path.join('image', 'median_amount_per_quarter.png'))
    plt.savefig(os.path.join('image', 'loans_per_quarter.png'))
    plt.show()

