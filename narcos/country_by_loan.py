import matplotlib.pyplot as plt
import os

def plot_country_by_loan_amount(df):
    country_df = df[['country', 'loan_amount']].groupby("country").sum()
    country_df['loan_ranked'] = df[['country', 'loan_amount']].groupby("country").sum().rank(ascending=True)
    country_df_filtered = country_df[country_df['loan_ranked'] < 20]
    # c = country_df.groupby("country").agg('sum')[['loan_amount']]/100000
    country_df_filtered.reset_index(inplace=True)
    print(country_df_filtered)

    country_df_filtered.plot.bar(x='country', y='loan_amount', color=['b', 'r', 'y', 'g', 'c', 'silver', 'm', 'k'],
                                 align='center', figsize=(20, 4))

    plt.title("Least funded 20 countries")
    plt.xlabel("Country Name")
    plt.ylabel("Loan Amount")
    plt.savefig(os.path.join('image', 'country_by_loan.png'))

    plt.show()
