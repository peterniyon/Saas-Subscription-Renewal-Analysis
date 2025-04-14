# Import required libraries
import pandas as pd

# Import data
client_details = pd.read_csv('data/client_details.csv')
subscription_records = pd.read_csv('data/subscription_records.csv', parse_dates = ['start_date','end_date'])
economic_indicators = pd.read_csv('data/economic_indicators.csv', parse_dates = ['start_date','end_date'])

# Create a function that counts "Fintech" or "Crypto" clients, in any dataframe containing client data.
def fintech_or_crypto(data_frame):
   """
   Count number of clients in Fintech or Crypto industries.
   """
   return data_frame['industry'].isin(['Fintech','Crypto']).sum()

total_fintech_crypto_clients = fintech_or_crypto(client_details)

print(f"There are a total of {total_fintech_crypto_clients} clients subscribed in fintech or crypto industries.")

# Merge client details with subscription records
subscriptions = pd.merge(subscription_records, client_details, on='client_id', how='left')

# Group by industry and calcalute renewal rate
industry_renewal_rates = subscriptions.groupby('industry')['renewed'].mean()

# Find the industry with the highest rate of subscription renewal
top_industry = industry_renewal_rates.sort_values(ascending = False).index[0]

print(f"The industry with the highest rate of subscription renewal is the {top_industry} industry.")

# Merge subscription records with economic indicators to get the inflation rate at the subscription end date (ie, renewal time)
subscriptions_with_inflation = pd.merge_asof(subscription_records.sort_values(by='end_date'), economic_indicators, left_on='end_date', right_on = 'start_date', direction = 'backward')

# Calcalute the average inflation rate for renewed subscriptions
average_inflation_for_renewals = subscriptions_with_inflation[subscriptions_with_inflation['renewed'] == True].inflation_rate.mean()

print(f"The average inflation rate for renewed subscriptions is: {average_inflation_for_renewals:.2%}.")
