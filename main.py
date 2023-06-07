from data_preprocess import clean_data
import pandas as pd

def main():
    # load data
    #clean data
    df = pd.read_csv('agoda_cancellation_train.csv')
    df = clean_data(df)



if __name__ == '__main__':
    main()