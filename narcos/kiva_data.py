'''

Kiva Data Module

Usage:

from kiva_data import KivaData
kiva_load_df = KivaData(sample=True.loan_data

'''

import os
import requests
import pandas as pd
from collections import Counter

SAMPLE_SIZE = 10000

class KivaData(object):
    
    def __init__(self, use_sample=False):
        self._use_sample = use_sample

    _loan_data = None
    
    @property
    def loan_data(self):
        if self._loan_data:
            return self._loan_data
        else:
            self._loan_data = self.get_loan_data()
            return self._loan_data
        
    @property
    def wb_data(self):
        if self._wb_dta:
            return self._wb_data
        else:
            self._wb_data = self.get_wb_data()           
  
    def get_loan_data(self):
        sample_str = '_sample' if self._use_sample else ''
        file = os.path.join('resource', f'kiva_loans{sample_str}.csv')
        df = pd.read_csv(file)

        ## Covert date time types
        time_columns = ['posted_time', 'disbursed_time', 'funded_time', 'date']
        df.loc[:, time_columns] = df[time_columns].apply(pd.to_datetime)
       
        ## Clean up gender
        # rule: With only 1 gender, convert to one multiple, take majority
        def normalize_gender(borrower_genders):
            if isinstance(borrower_genders, str):
                return Counter(
                    map(
                        lambda x: x.replace(' ', ''),
                        borrower_genders.split(', ')
                    )
                ).most_common(1)[0][0]
            else:
                return borrower_genders

        df.loc[:, 'gender'] = df['borrower_genders'].apply(normalize_gender)
        return df