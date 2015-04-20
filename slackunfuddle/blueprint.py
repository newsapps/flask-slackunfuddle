"""Flask Blueprint to proxy webhooks to Slack"""
import json

from flask import Blueprint, request

from .utils import slack_webhook_url, slack_webhook_post
from .transform import unfuddle_repo

blueprint = Blueprint('slackunfuddle', __name__)

# Match the Slack webhook URLs, like:
# /services/T0474V5VA/B04FA0KN6/SLqEI8WO7qElQJhcOye1ZhYM
# TODO: More meaningful parameter names than id1, id2, id3
@blueprint.route('/services/<id1>/<id2>/<id3>', methods=['POST'])
def webhook_proxy(id1, id2, id3):
    webhook_url = slack_webhook_url(id1, id2, id3)
    data = unfuddle_repo(request.data)
    payload = json.dumps(data)
    r = slack_webhook_post(webhook_url, payload)
    return r.text, r.status_code
