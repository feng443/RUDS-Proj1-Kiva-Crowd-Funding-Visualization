import pandas as pd
import numpy as np


country_info_df = pd.read_csv("../raw_data/HDI_complete.csv")
country_info_df.head()

def getTotalGDP(country,year):
    if year < 1990 or year > 2015:
        raise ValueError('The year is out of range')
    this_country_df = country_info_df[country_info_df["country"] == country]
    if len(this_country_df) == 0:
        return None
    gdp_df= this_country_df[this_country_df["kpi_name"] == "Gross Domestic Product (GDP), Total"]
    if len(gdp_df) == 0:
        return None
    if gdp_df[str(year)] is not None:
        return float(gdp_df[str(year)])
    else:
        return None


def getPerCapitaGDP(country,year):
    if year < 1990 or year > 2015:
        raise ValueError('The year is out of range')
    this_country_df = country_info_df[country_info_df["country"] == country]
    if len(this_country_df) == 0:
        return None
    gdp_df= this_country_df[this_country_df["kpi_name"] == "Gross Domestic Product (GDP) Per Capita"]
    if len(gdp_df) == 0:
        return None
    if (gdp_df[str(year)] is not None):
        return float(gdp_df[str(year)])
    else:
        return None

def getPerCapitaGNI(country,year):
    if year < 1990 or year > 2015:
        raise ValueError('The year is out of range')
    this_country_df = country_info_df[country_info_df["country"] == country]
    if len(this_country_df) == 0:
        return None
    gdp_df= this_country_df[this_country_df["kpi_name"] == "Gross National Income (Gni) Per Capita"]
    if len(gdp_df) == 0:
        return None
    if gdp_df[str(year)] is not None:
        return float(gdp_df[str(year)])
    else:
        return None


def getDevelopmentIndex(country,year):
    if year < 1990 or year > 2015:
        raise ValueError('The year is out of range')
    this_country_df = country_info_df[country_info_df["country"] == country]
    if len(this_country_df) == 0:
        return None
    gdp_df= this_country_df[this_country_df["kpi_name"] == "Human Development Index Score"]
    if len(gdp_df) == 0:
        return None
    if gdp_df[str(year)] is not None:
        return float(gdp_df[str(year)])
    else:
        return None

def getLatestPerCapitaGDP(country):
    return getPerCapitaGDP(country,2015)

def getLatestDevelopmentIndex(country,year):
    return getDevelopmentIndex(country,2015)
