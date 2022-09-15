import argparse
import requests
import json
import pandas as pd

def get_cmd_args():
  arg_parser = argparse.ArgumentParser(description='Lookup MAC addresses via API call.')
  arg_parser.add_argument('mac_list',type=str, help='Path to file containing a list of MAC addresses (one per line).')
  cmd_args = arg_parser.parse_args()
  return(cmd_args)

def file_input(mac_list_file_path = get_cmd_args().mac_list):
  with open(mac_list_file_path, 'r') as mac_list:
    mac_array = []
    lines = mac_list.readlines()
    for line in lines:
      mac_array.append(line.strip())
  return mac_array

def mac_vendor_get(mac_address_array,api_url="https://www.macvendorlookup.com/api/v2"):
  result = []
  for mac_address in mac_address_array:
    payload = {}
    headers = {}
    response = requests.request("GET", f"{api_url}/{mac_address}", headers=headers, data=payload)
    result.append(response.text)
  return(result)

def output_as_table(raw_json_array):
  json_result = []
  for i in raw_json_array:
    print(i)
  print(json_result)

output_as_table(mac_vendor_get(file_input()))
