[Hi.](http://dontpkethebear.com/wp-content/uploads/2014/03/4w.gif)

flask-slackunfuddle
===================

Proxy webhook requests from Unfuddle repositories to Slack.

Based on the [slackunfuddle](https://github.com/favoritemedium/slackunfuddle) Sinatra app.

Motivation
----------

Unfuddle can [post to a webhook](https://tribune.unfuddle.com/docs/topics/repository_callbacks) and Slack can [accept incoming webhooks](https://api.slack.com/incoming-webhooks).

However, Unfuddle posts XML in this format:

    <?xml version="1.0" encoding="UTF-8"?>
    <changeset>
      <author-id type="integer"> </author-id>
      <created-at type="datetime"> </created-at>
      <id type="integer"> </id>
      <message> </message>
      <repository-id type="integer"> </repository-id>
      <revision> </revision>
    </changeset>    

And Slack expects JSON in this format:

    curl -X POST --data-urlencode 'payload={"text": "This is posted to <#general> and comes from *monkey-bot*.", "channel": "#general", "username": "monkey-bot", "icon_emoji": ":monkey_face:"}' https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX

We need a simple web application to convert the Unfuddle XML to the JSON format expected by Slack.
