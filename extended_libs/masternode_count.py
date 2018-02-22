import requests
import json


def get_mn_count():
    mn_url = "https://stats.masternode.me/network-report/latest/json"

    response = requests.request("GET", mn_url)
    network_stats = json.loads(response.text)['formatted']
    mn_count = str(network_stats['f_mn_count']).replace(',', '')

    return mn_count
