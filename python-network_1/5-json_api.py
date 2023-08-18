#!/usr/bin/python3
"""
It's a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests
def search_user(letter):
    data = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"

    try:

        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            try:

                json_data = response.json()
                
                if json_data and 'id' in json_data and 'name' in json_data:

                    print(f"[{json_data['id']}] {json_data['name']}")
                else:

                    print("No result")
            except ValueError:

                print("Not a valid JSON")
        else:

            print(f"Error: {response.status_code}") 
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:

        search_user("")
    else:
        letter = sys.argv[1]
        search_user(letter)