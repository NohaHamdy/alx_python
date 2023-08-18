#!/usr/bin/python3
"""
It's a Python script that takes in a URL, sends a request to the URL and displays the body
"""
import sys
import requests
def fetch_url(url):
    try:

        response = requests.get(url)
        
        print(response.text)

        if response.status_code >= 400:

            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    fetch_url(url)