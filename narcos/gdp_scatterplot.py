import matplotlib.pyplot as plt
import pandas as pd
import os

def gdp_scatterplot(kiva_data):
    loan_data = kiva_data.loan_data
    gdp_lookup = {
        x[1]: x[2]
        for x in kiva_data.gdp[['country_code', 'gdp']].itertuples()
    }

    loan_gdp_df = loan_data.groupby(['country_code', 'gender'])['loan_amount'].agg(['median', 'count']).reset_index()

    loan_gdp_df.loc[:, 'gdp'] = loan_gdp_df['country_code'].map(
        lambda x: pd.to_numeric(gdp_lookup.get(x, 0))
    )
    loan_gdp_df = loan_gdp_df.query('gdp < 20000 & median < 4000')

    # Get size normalization factor

    size_factor = loan_gdp_df['count'].median() / 20

    figure, ax = plt.subplots(figsize=(16,10))

    for gender in ['female', 'male']:
        loan_gdp_df[
            loan_gdp_df['gender'] == gender
        ].plot.scatter(
            x='median',
            y='gdp',
            color='green' if gender == 'female' else 'steelblue',
            s = loan_gdp_df[loan_gdp_df['gender'] == gender]['count'] / size_factor,
            ax=ax,
            alpha=0.6,
            label=gender
        )

    plt.xlabel('Median Loan Amount')
    plt.ylabel('Per Capital GDP (2017 US$)')
    plt.title('Median Loan Amount vs GDP Per Capita (size by Number of Loans)')
    plt.savefig(os.path.join('image', 'gdp_scatterplot.png'))
    plt.show()