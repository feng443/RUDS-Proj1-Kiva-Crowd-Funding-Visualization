import matplotlib.pyplot as plt
import os

def plot_sector_by_loan_amount(df):
    sector_df = df[['sector','loan_amount']].groupby("sector").sum()
    sector_df['loan_ranked'] = df[['sector','loan_amount']].groupby("sector").sum().rank(ascending=True)
    sector_df_filtered = sector_df[sector_df['loan_ranked'] <20]
    #c = country_df.groupby("country").agg('sum')[['loan_amount']]/100000
    sector_df_filtered.reset_index(inplace=True)
    print(sector_df_filtered)

    sector_df_filtered.plot.bar(x='sector',y='loan_amount', color=['g'], align='center',figsize=(20,4))

    plt.title("Sector / Loan Plot")
    plt.xlabel("Sector Name")
    plt.ylabel("Loan Amount")
    plt.savefig(os.path.join('image', 'sector_by_loan.png'))

    plt.show()