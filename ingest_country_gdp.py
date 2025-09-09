import requests
import pandas as pd

# Fetch indicators from IMF API
url = "https://www.imf.org/external/datamapper/api/v1/indicators"
response = requests.get(url)

# Extract the indicators data from the JSON response
imf_indicator = response.json().get('indicators', {})

# Process the indicators into a DataFrame
imf_indicator_code = list(imf_indicator.keys())
imf_indicator_label = [v.get("label") for v in imf_indicator.values()]
imf_indicator_description = [v.get("description") for v in imf_indicator.values()]
imf_indicator_unit = [v.get("unit") for v in imf_indicator.values()]

df_imf_indicators = pd.DataFrame({'code': imf_indicator_code, 
                               'label': imf_indicator_label, 
                               'description': imf_indicator_description,
                               'unit': imf_indicator_unit})


# Fetch countries from IMF API
url = "https://www.imf.org/external/datamapper/api/v1/countries"
response = requests.get(url)

# Extract the countries data from the JSON response
imf_countries = response.json().get('countries', {})

# Process the countries into a DataFrame
imf_country_code = list(imf_countries.keys())
imf_country_name = [v.get("label") for v in imf_countries.values()]

df_imf_countries = pd.DataFrame({'code': imf_country_code, 
                               'name': imf_country_name})


# Fetch GDP data from IMF API
url = "https://www.imf.org/external/datamapper/api/v1/NGDPDPC"
response = requests.get(url)
indicator_code = "NGDPDPC"

# Extract the GDP data from the JSON response
imf_gdp_data = response.json().get('values', {}).get(indicator_code, {})


# Process the GDP data into a DataFrame
imf_gdp_country_code = list(imf_gdp_data.keys())
imf_gdp_2025 = [v.get("2025") for v in imf_gdp_data.values()]

df_imf_gdp = pd.DataFrame({'country_code': imf_gdp_country_code, 
                           'gdp_2025': imf_gdp_2025})
df_imf_gdp['indicator'] = indicator_code

