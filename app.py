from bottle import run, response,route
import os
from extended_libs import airtable
# from extended_libs import s3_integration as S3

@route('/votegraph', method="post")
def gen_graph():
    pass


@route('/votecheck', method="post")
def gen_vote_count():
    vote_data, current_ratio = airtable.save_to_airtable()
    clean_ratio = round(current_ratio,2)
    package = {"response_type": "in_channel", "text":
        "*Yes Votes:* {} \n *No Votes:* {} \n *Abstain Votes:* {} \n *Current Ratio* {}/10%".format(vote_data[0],
                                                                                                vote_data[1],
                                                                                                vote_data[2],
                                                                                                clean_ratio)}
    response.content_type = 'application/json'
    return package


if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)

