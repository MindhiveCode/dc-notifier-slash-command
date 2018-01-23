from bottle import run,post,request,response,route
import os
import requests
import json


def poll_dash_central():
    proposal_hash = 'ea1573f9cf32f83f3f35f1c8d6e7405dbd64a3ab26afb18019bd8ac5f551ac62'
    url = "https://www.dashcentral.org/api/v1/proposal?hash={}".format(proposal_hash)

    data = requests.get(url)
    data_dict = json.loads(data.text)

    vote_count_yes = data_dict['proposal']['yes']
    vote_count_no = data_dict['proposal']['no']
    vote_count_abstain = data_dict['proposal']['abstain']

    return vote_count_yes, vote_count_no, vote_count_abstain


@route('/votecheck', method="post")
def gen_vote_count():
    vote_count_yes, vote_count_no, vote_count_abstain = poll_dash_central()
    package = {"response_type": "in_channel", "text": "Yes Votes: {} \n No Votes: {} \n Abstain Votes: {}".format(vote_count_yes, vote_count_no, vote_count_abstain)}
    response.content_type = 'application/json'
    return package


if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)

