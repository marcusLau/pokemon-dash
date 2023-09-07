# Extracting data from Pogoapi and gamepress for comprehensive dps data on the trigger of a hash difference from Pogoapi.
import requests
import json
import csv
import pandas as pd
        
# Steps for extract file:
# need to pull all data and save it as JSON->CSV in data 
# extract file will TRIGGER on the difference of hashes       
        
def export():
    # function to do a get request to an api endpoint, path the path to write to
    # TODO: take all the downloaded data and insert into a database to apply SQL on
    URL = "https://pogoapi.net/api/v1/api_hashes.json"
    r = requests.get(url=URL)
    json_data = r.json()
    # print(type(json_data)) # type dict
    # df = pd.read_json(json_data)
    df = pd.DataFrame(json_data)
    print(df.T)
    df.T.to_csv('./data/hashes.csv')
    
    # json_data = json.load(r)
    
    # TODO: figure out how to write downloaded data into a folder to then upload into MYSQL
    
    # with open('G:\Akhil\jsonoutput.json') as json_file:
    #     jsondata = json.load(json_file)
 
    # data_file = open('data/hashes.csv', 'w', newline='')
    # csv_writer = csv.writer(data_file)
    
    # count = 0
    # for data in json_data:
    #     if count == 0:
    #         header = data.keys()
    #         csv_writer.writerow(header)
    #         count += 1
    #     csv_writer.writerow(data.values())
    
    # data_file.close()
    # return data
    
if __name__ == "__main__":
    export()