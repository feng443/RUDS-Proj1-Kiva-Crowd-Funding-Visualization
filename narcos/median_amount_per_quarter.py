import os
import matplotlib.pyplot as plt
<<<<<<< HEAD:narcos/medianamountperquarter.py
import numpy as np
import seaborn as sns
import os
from datetime import datetime
=======
>>>>>>> c1aace502f23501f00df55612ac10aac7e19ffb7:narcos/median_amount_per_quarter.py
import pandas as pd

def median_amount_per_quarter(df):
    df['mnth_yr2'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))

    # Add a column for quarter.
    df['Qtr'] = pd.PeriodIndex(pd.to_datetime(df.mnth_yr2), freq='Q')

    #Dataframe grouped by quarter. Takes the mediam loan amount per quarter.
    medloanq = df.groupby('Qtr').agg('median')[['loan_amount']]

    medloanq.plot.bar(y='loan_amount', figsize=(20, 15))
    plt.title('Median Loan Amount Per Quarter')
    plt.ylabel("Loan Amount")
    plt.xlabel("Quarter")
<<<<<<< HEAD:narcos/medianamountperquarter.py
    savepath = os.path.join('..', 'image')
    plt.savefig(savepath + 'median_amount_per_quarter_bar.png)
    # plt.savefig('numloans.png')
    # df.plot(figsize=(20,4))

    plt.show()


=======
    plt.savefig(os.path.join('image', 'median_amount_per_quarter.png'))
    
    plt.show()
>>>>>>> c1aace502f23501f00df55612ac10aac7e19ffb7:narcos/median_amount_per_quarter.py
