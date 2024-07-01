import requests
import pandas as pd
import logging

def fetch_industry_sales(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv('data/industry_sales.csv', index=False)
        logging.info("Industry sales data extracted successfully")
    except Exception as e:
        logging.error(f"Error fetching industry sales data: {e}")
