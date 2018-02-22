import requests
import json
import time
from extended_libs.dash_central import poll_dash_central
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
    current_ratio = round((((current_yes-current_no)/min_quorum)*10), 2)

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


def load_from_airtable():

    url = base_url + historical_data_view_uri

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer keyPAPufTGNL6ZwTO",
    }

    x_coordinates = []
    y_coordinates = []

    while True:
        try:
            response = requests.request("GET", url, headers=headers)
            record_list = json.loads(response.content)
            break
        except:
            print("Failed to fetch records, going to try again in 10 seconds.")
            time.sleep(10)

    print(record_list)

    try:
        offset = record_list['offset']  # get offset from first run to pass onto the next function which loops and grabs the rest until 'offset' = False
    except:
        offset = False

    print("Original offset = " + str(offset))  # - for debugging purposes only

    num_records = 0

    # This method is here to handle everything up until we have 100+ records and we start getting offsets
    if offset is False:
        # Keep it simple
        for rec in record_list['records']:
            num_records += 1
            x_coordinates.append((rec['fields']['Current Ratio'], rec['fields']['Yes Count'],
                                  rec['fields']['No Count'], rec['fields']['No Count'], rec['fields']['Abstain Count']))
            y_coordinates.append(rec['fields']['Timestamp'])

        return x_coordinates, y_coordinates


    # This is for handling offsets and 100+ records
    else:

        while True:
            if offset:
                for each_record in record_list['records']:
                    try:
                        num_records += 1
                        x_coordinates.append((rec['fields']['Current Ratio'], rec['fields']['Yes Count'],
                                              rec['fields']['No Count'], rec['fields']['No Count'],
                                              rec['fields']['Abstain Count']))
                        y_coordinates.append(rec['fields']['Timestamp'])
                    except:
                        print("Came across a blank record, moving on.")

                data = {'offset': offset}
                record_list = json.loads(requests.request("GET", url, headers=headers, params=data).content)

                try:
                    offset = record_list[
                        'offset']  # We re-set the offset every time we loop through although I feel like it shouldn't really work?
                    print("Current offset = " + offset)  # - for debugging purposes only
                except:
                    # Run one last time to get the records that weren't included in the offset range
                    for each_record in record_list['records']:
                        try:
                            num_records += 1
                            x_coordinates.append((rec['fields']['Current Ratio'], rec['fields']['Yes Count'],
                                                  rec['fields']['No Count'], rec['fields']['No Count'],
                                                  rec['fields']['Abstain Count']))
                            y_coordinates.append(rec['fields']['Timestamp'])
                        except:
                            print("Came across a blank record, moving on.")

                    print("Number of records read: {}".format(num_records))
                    return x_coordinates, y_coordinates
            else:
                break
