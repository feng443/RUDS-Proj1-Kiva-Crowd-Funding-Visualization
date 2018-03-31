'''

A utility class to convert alpha 2 contry code to alpha 2 wither buffering

<Chan Feng> 2018-03-30

'''

import requests

URL = 'http://api.worldbank.org/v2/countries/'

class CountryCodeConverter(object):

    _alpha_dict = {}
    
    @property
    def alpha_dict(self):
        return self._alpha_dict
    
    def __init__(self, countries):
        for cc in countries:
            ret = requests.get(f'{URL}{cc}?format=json')
            self._alpha_dict[cc] = ret.json()[1][0]['id']
            
    # TODO: Add on the go buffering
    def convert_alpha2_to_3(self, alpha2):
        return self._alpha_dict[alpha2]