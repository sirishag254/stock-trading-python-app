import time
import requests
import os
import csv
from dotenv import load_dotenv

load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
limit = 1000

url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={limit}&sort=ticker&apiKey={POLYGON_API_KEY}'

tickers = []

response = requests.get(url)
data = response.json()
#print(data)

while 'next_url' in data:
    
    time.sleep(15)
    print("printing next page")
   
    response = requests.get(data['next_url']+f'&apikey={POLYGON_API_KEY}')
    data = response.json()
    for ticker in data['results']:
        tickers.append(ticker)


example_ticker = {'ticker': 'SUSB', 
                  'name': 'iShares Trust iShares ESG Aware 1-5 Year USD Corporate Bond ETF', 
                  'market': 'stocks', 
                  'locale': 'us', 
                  'primary_exchange': 'XNAS', 
                  'type': 'ETF',
                  'active': True, 
                  'currency_name': 'usd', 
                  'cik': '0001100663', 
                  'composite_figi': 'BBG00H4BFKY5', 
                  'share_class_figi': 'BBG00H4BFM35', 
                  'last_updated_utc': '2025-09-18T06:05:34.657841073Z'
                  }

field_names = list(example_ticker.keys())
output_csv = 'tickers.csv'

with open(output_csv,mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    for t in tickers:
        print(len(tickers))
        row = {key: t.get(key, '') for key in field_names}
        writer.writerow(row)

print(f'wrote {len(tickers)} to {output_csv}') 

        




