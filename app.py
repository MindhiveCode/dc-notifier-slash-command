from bottle import run,post,request,response,route
import os
import requests


def


@route('/votecheck',method="post")
def gen_vote_count():
    package = {"response_type": "in_channel", "text": "{}".format(vote_count)}
    response.content_type = 'application/json'
    return package


if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)