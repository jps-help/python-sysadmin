import requests
import json
import pandas as pd

def mac_vendor_get(mac_address,api_url="https://www.macvendorlookup.com/api/v2"):
  payload={}
  headers = {}
  response = requests.request("GET", f"{api_url}/{mac_address}", headers=headers, data=payload)

  return(response.text)

def output_as_table(raw_json):
  data=json.loads(raw_json)  
  print(pd.DataFrame(data, columns=['startHex','endHex','company']))