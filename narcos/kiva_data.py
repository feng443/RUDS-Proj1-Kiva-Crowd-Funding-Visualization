'''

Kiva Data Mobule

Usage:
from kiva_data import KivaData
kiva_load_df = KivaData(sample=True.loan_data

'''

import os
import requests
import pandas as pd
from collections import Counter
from narcos.fixer_config import FIXER_KEY

FIXER_URL = "http://data.fixer.io/api/latest?"
SAMPLE_SIZE = 10000

class KivaData(object):
    
    def __init__(self, use_sample=False):
        self._use_sample = use_sample

    _exchange_rates = None
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
    
    @property
    def exchange_rates(self):
        if self._exchange_rates:
            return self._exchange_rates
        else:
            self._exchange_rates = self.get_rates()
            return self._exchange_rates
    
    def get_rates(self):
        ret_dict = {}
        
        query_url = FIXER_URL + "access_key=" + FIXER_KEY
        currency_response = requests.get(query_url)
        currency_json = currency_response.json()
        usd_val = currency_json["rates"]["USD"]
        for (key, value) in currency_json["rates"].items():
            ret_dict.update({key:(usd_val/value)})
    
        return ret_dict             
  
    def get_loan_data(self):
        sample_str = '_sample' if self._use_sample else ''
        #file = os.path.join('raw_data', f'kiva_loans{sample_str}.csv')
        file = os.path.join('raw_data', 'kiva_loans_sample.csv')
        df = pd.read_csv(file)

        ## Covert date time types
        time_columns = ['posted_time', 'disbursed_time', 'funded_time', 'date']
        df.loc[:, time_columns] = df[time_columns].apply(pd.to_datetime)

        ## Convert to USD
        for amount in  ['funded_amount', 'loan_amount']:
            df.loc[:, amount] = df[amount] * df['currency'].apply(
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
        return df