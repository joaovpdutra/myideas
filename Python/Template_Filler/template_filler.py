import pandas as pd

dataframe= pd.read_excel("C:/Users/joao/OneDrive/Documentos/GitHub/myideas/Python/db_example_applications.xlsx")

def filltemplatepdf(recordid):
    select_record = dataframe.loc[dataframe['id'] == recordid]
    print(recordid)
    print(select_record)

