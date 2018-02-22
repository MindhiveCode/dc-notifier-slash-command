import json
import requests

def poll_dash_central():
    proposal_hash = '4e2f9d85b393c40fd9ef5f24b85d1fcd01658500584f072dae223deb2cd8b842'
    url = "https://www.dashcentral.org/api/v1/proposal?hash={}".format(proposal_hash)

    data = requests.get(url)
    data_dict = json.loads(data.text)

    vote_count_yes = data_dict['proposal']['yes']
    vote_count_no = data_dict['proposal']['no']
    vote_count_abstain = data_dict['proposal']['abstain']

    return vote_count_yes, vote_count_no, vote_count_abstain

