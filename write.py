import openpyxl
import pandas as pd

def export(dataframe):

    car_name = 'Honda'
    model_name = 'ACCORD Coupe(CM)(2003-2008)2'
    
    columns = ['Name', 'Part Number']

    df = pd.DataFrame(dataframe, columns=columns)
    print(df)
    with pd.ExcelWriter('Honda\Accord\Accord.xlsx', engine='openpyxl',mode='a', if_sheet_exists = 'replace') as writer:
        df.to_excel(writer, sheet_name=model_name)