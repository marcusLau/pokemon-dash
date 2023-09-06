import requests

URL = "https://pogoapi.net/api/v1/api_hashes.json"

r = requests.get(url=URL)

data = r.json()
# print(data)

# Now need to write this logic into an Airflow typa methodology to check daily if any updates
# if so, then airflow starts the download across all json and comphrensive dps
    # then transforms the data
        # then loads into a new database with a new version number etc. 