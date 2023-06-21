import pandas as pd
import logging
import urllib.request

# Set up logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
log = logger.info

# Use
# from main import dataset
# In your script to read the dataset


def dataset():
    gist_url = "https://gist.githubusercontent.com/balmasi/0e65f72c48f2a3498ceb36ffc216f5eb/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv"
    titanic_data = pd.read_csv(urllib.request.urlopen(gist_url))
    return titanic_data


# Comment the description below to omit log messages
if __name__ == "__main__":

    try:
        # Read Titanic dataset from Gist URL
        titanic_data = dataset()

        # Perform exploratory data analysis
        log("Data Description:")
        # log(titanic_data.describe())

        log("Column Information:")
        # log(titanic_data.info())

        log("Null Value Counts:")
        # log(titanic_data.isnull().sum())

    except Exception as e:
        log(f"Error occurred: {str(e)}")


    log("--------------------------------")

