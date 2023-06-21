import pandas as pd
import logging
import urllib.request

# Set up logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
log = logger.info

# Gist URL of the Titanic dataset
gist_url = "https://gist.githubusercontent.com/balmasi/0e65f72c48f2a3498ceb36ffc216f5eb/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv"

try:
    # Read Titanic dataset from Gist URL
    titanic_data = pd.read_csv(urllib.request.urlopen(gist_url))

    # Perform exploratory data analysis
    log("Data Description:")
    log(titanic_data.describe())

    log("Column Information:")
    log(titanic_data.info())

    log("Null Value Counts:")
    log(titanic_data.isnull().sum())

except Exception as e:
    log(f"Error occurred: {str(e)}")


log("--------------------------------")
log("------ titanic_data ----------")
log(titanic_data.head())



