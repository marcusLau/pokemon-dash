# Extracting data from Pogoapi and gamepress for comprehensive dps data on the trigger of a hash difference from Pogoapi.
import requests
import json
import csv

# print(data)

# Now need to write this logic into an Airflow typa methodology to check daily if any updates
# if so, then airflow starts the download across all json and comphrensive dps
    # then transforms the data
        # then loads into a new database with a new version number etc. 
        
        
def export(url):
    # function to do a get request to an api endpoint, path the path to write to
    # TODO: take all the downloaded data and insert into a database to apply SQL on
    URL = "https://pogoapi.net/api/v1/api_hashes.json"
    r = requests.get(url=URL)
     # json_data = r.json()
    
    json_data = json.load(r)
    
    # TODO: figure out how to write downloaded data into a folder to then upload into MYSQL
    
    # with open('G:\Akhil\jsonoutput.json') as json_file:
    #     jsondata = json.load(json_file)
 
    data_file = open('data/hashes.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)
    
    count = 0
    for data in json_data:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    
    data_file.close()
    # return data
    


if __name__ == "__main__":
    export("https://pogoapi.net/api/v1/api_hashes.json")