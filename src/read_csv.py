import pandas as pd

def read_csv(file_address:str, column:int):

    """ Takes an address of csv file and column number
        then returns the column"""
    
    df = pd.read_csv(file_address)
    column_data = df.iloc[:, column]
    
    return column_data  

