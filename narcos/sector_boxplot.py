import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

def sector_boxplot(loan_data):
    figure, ax = plt.subplots(figsize=(20,10))

    sns.boxplot(
        x='sector', 
        y='funded_amount',
        color='steelblue',
        data=loan_data[loan_data['funded_amount'] < 5000])

    plt.title('Distibuction of Loan Amount by Sector')
    plt.ylabel('Loan Amount (US$)')
    plt.xlabel('')
    plt.savefig(os.path.join('image', 'sector_boxplot.png'))
    
    plt.show()