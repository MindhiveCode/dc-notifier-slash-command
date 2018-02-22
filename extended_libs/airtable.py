import requests
import json
import time
from app import poll_dash_central
from extended_libs.masternode_count import get_mn_count

base_url = "https://api.airtable.com/v0/appLGmMyGYx8w1EVH/"
historical_data_view_uri = "VoteHistory"
record = "reccK5SigbEdjyv6t"


def save_to_airtable():
    current_data = poll_dash_central()

    min_quorum = int(get_mn_count())/10

    current_yes = current_data[0]
    current_no = current_data[1]
    current_abstain = current_data[2]
    current_ratio = ((current_yes-current_no)/min_quorum)*10

    payload = json.dumps({"fields": {"Current Ratio": current_ratio, "Yes Count": current_yes, "No Count": current_no,
                                     "Abstain Count": current_abstain}})

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer keyPAPufTGNL6ZwTO",
    }

    post_url = base_url + historical_data_view_uri

    while True:
        try:
            response = requests.request("POST", post_url, data=payload, headers=headers)
            break
        except:
            print("Failed to save records, going to try again in 10 seconds.")
            time.sleep(10)

    if response.status_code == 200:
        return current_data, current_ratio
    else:
        print(response.status_code)
        print(response.text)
        return 0


save_to_airtable()