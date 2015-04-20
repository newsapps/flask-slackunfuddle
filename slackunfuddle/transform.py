"""
Transformation functions for Slack incoming webhooks

Functions should take a string as input and return a dictionary that can be
serialized as JSON.

This serialized JSON should match the format documented at 
https://api.slack.com/incoming-webhooks

"""
from lxml import etree

from .utils import unfuddle_commit_url

def parse_unfuddle_changeset(s):
    """
    Parse Unfuddle changeset XML into a dictionary

    Args:
        s: String containing XML data describing the changeset.
           See https://tribune.unfuddle.com/docs/api/data_models#changeset
           for data format.

    Returns:
        Dictionary where the keys match the child elements of the changeset
    """
    d = {}
    tree = etree.fromstring(s)
    for el in tree:
        d[el.tag] = el.text
    return d    


def unfuddle_repo(s, **kwargs):
    """
    Transform data posted by Unfuddle on a changeset to a Slack message
    
    Args:
        s: String containing XML data describing the changeset.
           See https://tribune.unfuddle.com/docs/api/data_models#changeset
           for data format.

    Returns:
       Dictionary that can be serialized into JSON representing a Slack
       message

    """
    changeset = parse_unfuddle_changeset(s)
    commit_url = unfuddle_commit_url(changeset['subdomain'],
        changeset['repository-id'], changeset['revision'])
    message_tpl = "{committer_name} pushed <{commit_url}|{revision}> to {branch}: {message}"
    payload = dict(**kwargs)
    payload['text'] = message_tpl.format(
       committer_name=changeset['committer-name'],
       commit_url=commit_url,
       revision=changeset['revision'][0:5],
       branch=changeset['branch'],
       message=changeset['message']
    ) 
    return payload
