from bottle import run, response, route
import os
import json
from extended_libs import airtable
from extended_libs import s3_integration as S3
#from extended_libs import dash_plot
from extended_libs import  dash_central

def generate_slack_message(graph_url):
    slack_attachment = []
    vote_data, current_ratio = airtable.save_to_airtable()

    text = "*Yes Votes:* {} \n *No Votes:* {} \n *Abstain Votes:* {} \n *Current Ratio* {}/10%".format(vote_data[0],
                                                                                                       vote_data[1],
                                                                                                       vote_data[2],
                                                                                                       current_ratio)
    slack_attachment.append({
        "pretext": "*Voting Update*",
        "color": "{}".format('#fcc118'),
        "text": text,
        "footer": "Vote Updater",
        "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
        "mrkdwn_in": ["pretext"],
        "title": "{}".format("Vote Graph"),
        "image_url": "{}".format(graph_url)
    })

    package = {"response_type": "in_channel", "text": "Latest Charts", "attachments": json.dumps(slack_attachment)}

    return package


@route('/votegraph', method="post")
def gen_graph():
    plot_url = dash_plot.gen_plot_n_upload()
    package = generate_slack_message(plot_url)
    response.content_type = 'application/json'
    return package


@route('/votecheck', method="post")
def gen_proposal_data():
    proposal_data = dash_central.poll_dash_central()
    airtable.save_to_airtable(proposal_data)

    package = {"response_type": "in_channel", "text":
        "*Yes Votes:* {} \n".format(proposal_data['yes']) +
        "*No Votes:* {} \n".format(proposal_data['no']) +
        "*Abstain Votes:* {} \n ".format(proposal_data['abstain']) +
        "*Current Ratio:* {}/10% \n".format(proposal_data['current_ratio']) +
        "*Votes Until Funding:* {} \n".format(proposal_data['remaining_yes_votes_until_funding']) +
        "*Number of Comments:* {} \n".format(proposal_data['comment_amount']) +
        "*Voting Deadline:* {} \n".format(proposal_data['voting_deadline_human']) +
        "*Link:* {}".format(proposal_data['url'])

               }

    response.content_type = 'application/json'
    return package


if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)
