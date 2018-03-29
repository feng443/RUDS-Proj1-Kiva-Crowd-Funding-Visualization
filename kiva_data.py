'''

Kiva Data Mobule

Usage:
from kiva_data import KivaData
kiva_load_df = KivaData(sample=True.loan_data


'''

import os
import pandas as pd
from collections import Counter

SAMPLE_SIZE = 10000

class KivaData(object):
    @property
    def loan_data(self):
        return self._loan_data

    def __init__(self, use_sample=False):
        sample_str = '_sample' if use_sample else ''
        file = os.path.join('raw_data', f'kiva_loans{sample_str}.csv')
        df = pd.read_csv(file)

        ## Covert date time types
        time_columns = ['posted_time', 'disbursed_time', 'funded_time', 'date']
        df.loc[:, time_columns] = df[time_columns].apply(pd.to_datetime)

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