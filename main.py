import yaml
import logging
from scripts.industry_sales import fetch_industry_sales
from scripts.economic_indicators import fetch_economic_indicators

# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Setup logging
logging.basicConfig(filename=config["log_file"], level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    logging.info("Starting data collection process")
    fetch_industry_sales(config["data_sources"]["industry_sales"]["url"])
    fetch_economic_indicators(config["data_sources"]["economic_indicators"]["url"])
    logging.info("Data collection process finished")

if __name__ == "__main__":
    main()
