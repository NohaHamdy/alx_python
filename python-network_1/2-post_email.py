#!/usr/bin/python3
"""
It's a Python script that takes in a URL and an email address, sends a POST request
"""
import sys
"""
Importing package of  sys 
"""
import requests
"""
importing package of request
"""
def send_post_request(url, email):

    data = {'email': email}
    try:

        response = requests.post(url, data=data)

        if response.status_code == 200:

            print(response.text)
        else:

            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python script.py <url> <email>")
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)