import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import pandas as pd

from narcos.kiva_data import KivaData
df = KivaData(use_sample=True).loan_data
df.describe()

def medloanquarter():

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')
    df.head()

    #Dataframe grouped by quarter. Takes the mediam loan amount per quarter.
    medloanq = df.groupby('Qtr').agg('median')[['loan_amount']]
    medloanq.head()

    medloanq.plot.bar(y='loan_amount', figsize=(20, 4))
    plt.title('Median Loan Amount Per Quarter')
    plt.ylabel("Loan Amount")
    plt.xlabel("Quarter")
    # plt.savefig('numloans.png')
    # df.plot(figsize=(20,4))

    plt.show()


