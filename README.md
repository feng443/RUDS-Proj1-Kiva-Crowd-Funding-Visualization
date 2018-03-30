# Rutgers Data Science Bootcamp Project #1 - Kiva Crowdfunding Analystics

March - April 2018, Team NACOS:

- [Chan Feng](https://github.com/feng443)
- [Anuj Pandya](https://github.com/anujpandya3105)
- [Nisha Agarwal](https://github.com/agarwan1)
- [Ravi Kolla](https://github.com/ravikanth-kolla)

## Synopsis
Based on Wikipedia, Kiva is a non profit organization that allows people to lend money via the Internet to low-income entrepreneurs and students in over 80 countries. Kiva's mission is “to connect people through lending to alleviate poverty".

In this analysis, we will look into patterns of Kiva crowd-funding utlizing [Kaggle data set](https://www.kaggle.com/kiva/data-science-for-good-kiva-crowdfunding), [Fixer Foreign Exchange API](https://fixer.io/) and [World Bank Open Data](https://data.worldbank.org/).

## Questions

- Comparison by country, sector ad gender
- Distribution of loans geographically on a global map
- Word Cloud to show what keywords are mostly mentioned
- Histogram and barplots showing distribution of load amount
- Trend over time
- Correlation of median loan amount vs GDP per capital and country's level of development (based on Word Bank)

## Development Methods

- Make it work first, then improve
- Fast iteration
- Modular and test driven

## Code Organization

* Kiva_Analytics.ipynb
* README.md
* config.py
* lib/
    * kiva_data.py
    * map.py
    * wordcloud.py
* raw_data/
* test/
