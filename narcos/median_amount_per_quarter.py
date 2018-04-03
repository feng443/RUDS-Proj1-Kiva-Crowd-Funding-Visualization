import os
import matplotlib.pyplot as plt
import pandas as pd

def median_amount_per_quarter(df):
    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))

    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')

    #Dataframe grouped by quarter. Takes the mediam loan amount per quarter.
    medloanq = df.groupby('Qtr').agg('median')[['loan_amount']]

    medloanq.plot.bar(y='loan_amount', figsize=(20, 15))
    plt.title('Median Loan Amount Per Quarter')
    plt.ylabel("Loan Amount")
    plt.xlabel("Quarter")
    plt.savefig(os.path.join('image', 'median_amount_per_quarter.png'))
    
    plt.show()
