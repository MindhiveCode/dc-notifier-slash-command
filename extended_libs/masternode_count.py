import requests
import json


def get_mn_count():
    mn_url = "https://stats.masternode.me/network-report/latest/json"

    try:
        response = requests.request("GET", mn_url)

        if response.status_code is not 200:
            mn_count = 4700
        else:
            network_stats = json.loads(response.text)['formatted']
            mn_count = str(network_stats['f_mn_count']).replace(',', '')

    except:
        mn_count = 4700

    return mn_count
