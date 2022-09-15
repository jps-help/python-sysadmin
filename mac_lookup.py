import argparse
import re
import requests
import json
import pandas as pd

def get_cmd_args():
  arg_parser = argparse.ArgumentParser(description='Lookup MAC addresses via API call.')
  arg_parser.add_argument('mac_list', type=str, help='Path to file containing a list of MAC addresses (one per line).')
  arg_parser.add_argument('-f','--format', choices=['plain','standard','dash'], default='standard', help= 'Select an output format for MAC addresses to displayed in.')
  cmd_args = arg_parser.parse_args()
  return(cmd_args)

def format_mac(mac: str,format):
  mac = re.sub('[.:-]', '', mac).lower()  # remove delimiters and convert to lower case
  mac = ''.join(mac.split())  # remove whitespaces
  assert len(mac) == 12  # length should be now exactly 12 (eg. 008041aefd7e)
  assert mac.isalnum()  # should only contain letters and numbers
  
  # Return MAC in plain format.
  def plain(mac):
    return(mac)
  # Return MAC in standard colon separated format.
  def standard(mac):
    return(":".join(["%s" % (mac[i:i+2]) for i in range(0, 12, 2)]))
  # Return MAC in dash separated format.
  def dash(mac):
    return("-".join(["%s" % (mac[i:i+2]) for i in range(0, 12, 2)]))

  options = {'plain'   : plain,
             'standard': standard,
             'dash'    : dash
  }
  return(options[format](mac))

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

