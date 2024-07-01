import requests
import pandas as pd
import logging

def fetch_economic_indicators(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv('data/economic_indicators.csv', index=False)
        logging.info("Economic indicators data extracted successfully")
    except Exception as e:
        logging.error(f"Error fetching economic indicators data: {e}")
