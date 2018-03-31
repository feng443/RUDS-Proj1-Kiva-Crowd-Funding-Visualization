'''

Kiva Data Mobule

Usage:
from kiva_data import KivaData
kiva_load_df = KivaData(sample=True.loan_data


'''

import os
import pandas as pd
from collections import Counter
from forex_python.converter import CurrencyRates

SAMPLE_SIZE = 10000

class KivaData(object):
    
    _exchange_rates = None
    
    @property
    def loan_data(self):
        return self._loan_data
    
    @property
    def wb_data(self):
        if self._wb_dta:
            return self._wb_data
        else:
            self._wb_data = self.get_wb_data()
    
    @property
    def exchange_rates(self):
        if self._exchange_rates:
            return self._exchange_rates
        else:
            self._exchange_rates = self.get_rates()
            return self._exchange_rates
    
    def get_rates(self):
        
        # Get the rates from API
        
        # Store into self._rates for SSP, store hardcode most recent rate
        return {'USD': 1, 'CNY': 6.72}
        
  
    def __init__(self, use_sample=False):
        sample_str = '_sample' if use_sample else ''
        #file = os.path.join('raw_data', f'kiva_loans{sample_str}.csv')
        file = os.path.join('raw_data', 'kiva_loans_sample.csv')
        df = pd.read_csv(file)

        ## Covert date time types
        time_columns = ['posted_time', 'disbursed_time', 'funded_time', 'date']
        df.loc[:, time_columns] = df[time_columns].apply(pd.to_datetime)

         
        ## Convert to USD
        for amount in  ['funded_amount', 'loan_amount']:
            df.loc[:, amount + '_usd'] = df[amount] * df['currency'].apply(
                lambda x: self.exchange_rates.get(x, 1)
            )
        
        ## Clean up gender
        # rule: With only 1 gender, convert to one multiple, take majority
        def normalize_gender(borrower_genders):
        #return type(borrower_genders)
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
        
       
        
        self._loan_data = df
