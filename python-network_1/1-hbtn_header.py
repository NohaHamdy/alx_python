#!/usr/bin/python3
""" 
It's a Python script that takes in a URL, sends a request to the URL ,and displays the value
"""
import sys
import requests
def get_x_request_id(url):
    """
    Method to get x_request
    """
    try:
        """
        Send a GET request to the provided URL
        """
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        """
        Get the value of the X-Request-Id header from the response
        """
        if x_request_id:
            """
            If X-Request-Id header exists in the response, print its value
            """
            print(x_request_id)
        else:
            """If X-Request-Id header is not found, print a message"""
            print(None)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Check if the script is run with the correct number of arguments
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    """
    Get the URL from the command line arguments
    """
    get_x_request_id(url)