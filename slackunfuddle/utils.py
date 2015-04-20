import requests

def slack_webhook_url(id1, id2, id3):
    url_tpl = "https://hooks.slack.com/services/{}/{}/{}"
    return url_tpl.format(id1, id2, id3)


def slack_webhook_post(url, payload):
    """
    Post to a Slack incoming webhook endpoint

    For more information about the expected format of the payload, see
    https://api.slack.com/incoming-webhooks
    
    Args:
        url: String containing the URL of a Slack incoming webhook endpoint. For
            example:

            https://hooks.slack.com/services/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
        payload: String containing JSON that will be used as the payload of the
            payload parameter of the POST request.

    Returns:
        requests.Response object for the requested webhook
        
    """
    data = {
        'payload': payload    
    }
    r = requests.post(url, data=data)
    return r


def unfuddle_commit_url(subdomain, repository_id, revision):
    url_tpl = "https://{subdomain}.unfuddle.com/a#/repositories/{repository_id}/commit?commit={revision}"
    return url_tpl.format(subdomain=subdomain, repository_id=repository_id,
                   revision=revision)
