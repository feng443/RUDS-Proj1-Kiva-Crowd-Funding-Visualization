import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def number_loans_per_sector(df):

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')

    ts_df = df.groupby(['Qtr', 'sector'])['id'].count().reset_index()
    ts_df = ts_df[ts_df['Qtr'] < pd.Period('2017Q3')]
    
    plt.figure(figsize=(16, 10))
    sns.pointplot(
        x='Qtr',
        y='id',
        hue='sector',
        alpha=0.8,
        data=ts_df,
        palette="Set2")
    plt.title('Number of loans per Sector and Quarter')
    plt.ylabel('Number of Loans')
    plt.xlabel('Quarter')
    plt.savefig(os.path.join('image', 'number_loans_per_sector.png'))
    plt.show()
