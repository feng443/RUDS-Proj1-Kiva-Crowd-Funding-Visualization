# <Chan Feng> 2018-04-01 Plot Kiva loan in world map.
import pandas as pd
from narcos.country_code_converter import CountryCodeConverter

import plotly.plotly as py
import plotly
import plotly.graph_objs as go

import os

def plot_map(loan_data, by='sum'):
    plotly.tools.set_credentials_file(username='feng443', api_key='qjXE19UfO00GLS5YJKhw')

    amount_by_country = loan_data.groupby(['country_code', 'country'])['funded_amount'].agg(by).reset_index()

    CC = CountryCodeConverter(amount_by_country.country_code.unique())

    amount_by_country.loc[:, 'CC'] = amount_by_country.country_code.apply(CC.convert_alpha2_to_3)

    data = [ dict(
            type = 'choropleth',
            locations = amount_by_country['CC'],
            z = amount_by_country['funded_amount'],
            text = amount_by_country['country'],
            #colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            #    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
            #colorscale = [[0,"rgb(5, 10, 172)"], [0.1,"rgb(40, 60, 190)"], [1,"rgb(255, 0, 0sca)"]],
            
            autocolorscale = True,
            reversescale = False,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '$',
                title = 'Funded Amount'),
          ) ]

    layout = dict(
        title = f'Kiva Funded Amount ({by}) per Country',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )

    fig = dict(data=data, layout=layout)
    py.image.save_as(fig, filename=os.path.join('image', f'map_amount_{by}_by_country.png'))
    return fig
    # py.iplot(fig, validate=False, filename='d3-world-map' )