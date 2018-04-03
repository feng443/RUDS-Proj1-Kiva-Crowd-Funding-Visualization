import matplotlib.pyplot as plt
import os

def sector_bar(loan_data):
    fig = plt.figure(figsize=(20,8))
    fig.suptitle("Kiva Loan Statistics by Sector and Gender")

    ax1 = plt.subplot2grid((2, 1), (0, 0))
    loan_data.groupby(
        ['sector', 'gender']
    )['funded_amount'].agg(
        ['median']
    ).reset_index(
    ).pivot(
        index='sector',
        columns='gender'    
    ).plot.bar(
        ax=ax1,
        stacked=False,
        color=['green', 'steelblue']
    )
    ax1.tick_params(
        axis='x',
        labelbottom='off',
        bottom='off'
    )
    plt.ylabel('US$')
    plt.title('Median Loan Amount Per Sector')

    ax2 = plt.subplot2grid((2, 1), (1, 0))
    loan_data.groupby(
        ['sector', 'gender']
    )['funded_amount'].agg(
        ['count']
    ).reset_index(
    ).pivot(
        index='sector',
        columns='gender'    
    ).plot.bar(
        ax=ax2,
        stacked=True
    )

    plt.ylabel('Number of Loans')
    plt.title('Number of Loans per Sector')
    
    plt.savefig(os.path.join('image', 'sector_bat.png'))
    plt.show()