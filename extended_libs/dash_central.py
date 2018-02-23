import json
import requests
from extended_libs import masternode_count

def poll_dash_central():
    proposal_hash = '4e2f9d85b393c40fd9ef5f24b85d1fcd01658500584f072dae223deb2cd8b842'
    url = "https://www.dashcentral.org/api/v1/proposal?hash={}".format(proposal_hash)

    data = requests.get(url)
    proposal_data = json.loads(data.text)['proposal']


    min_quorum = int(masternode_count.get_mn_count())/10
    proposal_data['current_ratio'] = round((((proposal_data['yes']-proposal_data['no'])/min_quorum)*10), 2)

    '''
    vote_count_yes = data_dict['proposal']['yes']
    vote_count_no = data_dict['proposal']['no']
    vote_count_abstain = data_dict['proposal']['abstain']
    '''

    return proposal_data

poll_dash_central()

