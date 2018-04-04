import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

def sector_boxplot(loan_data):
    figure, ax = plt.subplots(figsize=(14,8))

    sns.boxplot(
        x='sector', 
        y='loan_amount',
        color='steelblue',
        data=loan_data[loan_data['loan_amount'] < 5000])

    plt.title('Distibuction of Loan Amount by Sector')
    plt.ylabel('Loan Amount (US$)')
    plt.xlabel('')
    plt.savefig(os.path.join('image', 'sector_boxplot.png'))
   
    plt.show()