#pip install pymongo
import pymongo
from pymongo import MongoClient
import pandas as pd
import json


client = pymongo.MongoClient("mongodb+srv://mriganka99:sOcnFXwgYlLnVqv8@cluster0.0xbu9ow.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"C:\Users\mriga\Videos\Data Science\Project\Insurance Project\Insurance-Project\insurance.csv")

DATABASE_NAME = 'INSURANCE'
COLLECTION_NAME = 'INSURANCE_PROJECT'


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows & Columns: {df.shape}")
    
    df.reset_index(drop= True, inplace= True)
    
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
