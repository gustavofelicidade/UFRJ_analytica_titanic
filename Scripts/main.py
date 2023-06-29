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

    gist_url_train = "https://gist.githubusercontent.com/gustavofelicidade/3894049b7c0f09a9bbed74b402345c4b/raw/513d7e17fc431ff12a1619c2663af328b880b019/train.csv"
    gist_url_test = "https://gist.githubusercontent.com/gustavofelicidade/3894049b7c0f09a9bbed74b402345c4b/raw/513d7e17fc431ff12a1619c2663af328b880b019/test.csv"
    train = pd.read_csv(urllib.request.urlopen(gist_url_train))
    test = pd.read_csv(urllib.request.urlopen(gist_url_test))
    return train, test


# Comment the description below to omit log messages
if __name__ == "__main__":

    try:
        # Read Titanic dataset from Gist URL
        train, test = dataset()

        # Perform exploratory data analysis
        log("Data Description:")
        log(train.describe())
        log(test.describe())

        log("Column Information:")
        log(train.info())
        log(test.info())

        log("Null Value Counts:")

        log(train.isnull().sum())
        log(test.isnull().sum())

    except Exception as e:
        log(f"Error occurred: {str(e)}")


    log("--------------------------------")

