import matplotlib.pyplot as plt
import os

def loans_by_gender(df):
    df.groupby('gender').agg('count')[['loan_amount']].plot.pie(y='loan_amount')

    plt.savefig(os.path.join('image', 'sector_by_loan.png'))

    plt.show()