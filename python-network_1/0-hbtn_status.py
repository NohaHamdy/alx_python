#!/usr/bin/python3
"""It's a Python script that fetches https://alu-intranet.hbtn.io/status"""

import requests
"""importing package of request"""
url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)
if response.status_code == 200:

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
else:
    print(f"Error: {response.status_code}")