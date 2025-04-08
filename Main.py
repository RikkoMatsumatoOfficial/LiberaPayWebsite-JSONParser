import requests as req
import os
from os import _exit as exitfunc

def get_data_from_url(url):
    response = req.get(url)
    response_data_split_by_line = response.content.decode('utf-8').splitlines()
    return response_data_split_by_line

def Main():
    username_liberapay = input("Please Write You're LiberaPay USERNAME: ")
    try:
        request_resp = get_data_from_url("https://liberapay.com/{}/public.json".format(username_liberapay))
        print(request_resp)
    except:
        print("Failed to Get You're Data about you're LiberaPay Account!!! Please Register in Liberapay!!!")
        exitfunc(3441)

if __name__ == "__main__":
    Main()