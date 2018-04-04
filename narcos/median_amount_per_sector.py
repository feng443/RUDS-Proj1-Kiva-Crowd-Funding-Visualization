import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def median_amount_per_sector(df):

    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')
    #df.head()

    # Median Loan Amount of Sector per Quarter
    md_df = df.groupby(['Qtr', 'sector'])['loan_amount'].median().reset_index()
    md_df = md_df[md_df['Qtr'] < pd.Period('2017Q3')]
    md_df
    # funded_amount
    plt.figure(figsize=(16, 10))
    sns.pointplot(
        x='Qtr',
        y='loan_amount',
        hue='sector',
        alpha=0.8,
        data=md_df,
        palette="Set2")
    plt.title('Median Loan Amount per Sector and Quarter')
    plt.ylabel('Median Loan Amount')
    plt.xlabel('Quarter')
    plt.savefig(os.path.join('image', 'median_amount_per_sector.png'))

    plt.show()
