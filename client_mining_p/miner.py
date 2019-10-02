import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 

def get_last_block():
    response = requests.get("http://localhost:5000/last_block")
    if response:
        print('Success!')
        return response.json()
    else:
        print('An error has occurred.')

def get_the_proof():
    response = requests.get('http://localhost:5000/mine')
    returned_response = response.json()
    if returned_response.message == 'New Block Forged':
        print (returned_response.message)

get_last_block()


