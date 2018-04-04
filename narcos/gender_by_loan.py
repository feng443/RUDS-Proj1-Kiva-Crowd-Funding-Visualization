import matplotlib.pyplot as plt
import os

def loans_by_gender(df):
    df.groupby('gender').agg('count')[['loan_amount']].plot.pie(y='loan_amount', colors=['green','steelblue'], figsize=(3,3), autopct='%1.1f%%', legend=False)
    plt.axis('equal')
    plt.savefig(os.path.join('image', 'genders_by_loan.png'))
    
  
    plt.show()
