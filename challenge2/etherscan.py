import requests
import os

# import python requests

# get api key from env
api_key = os.environ.get("API_KEY")
# "5CV8ABV2VWSBF1S5GFPNPARVJVAW2A7483"


def print_transfer(transaction_hash):
    # call etherscan api to find transaction logs with transaction hash
    response = requests.get(
        f"https://api.etherscan.io/api?module=account&action=txlistinternal&txhash={transaction_hash}&apikey={api_key}"
    )
    # confirn status is OK
    if response.status_code == 200:
        # print result
        print(response.json()["result"])
        return
    if response.status_code == 403:
        print("unauthorized")
    else:
        print(response.text)
    return

    # get your api


print_transfer("0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263")
