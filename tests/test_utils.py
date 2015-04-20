from unittest import TestCase

from slackunfuddle.utils import slack_webhook_url

class UtilsTestCase(TestCase):
    def test_slack_webhook_url(self):
        expected_url = "https://hooks.slack.com/services/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"

        ids = [
            'T0474V5VA',
            'B04FA0KN6',
            'SLqEI8WO7qElQJhcOye1ZhYM'
        ]

        url = slack_webhook_url(*ids)
        self.assertEqual(url, expected_url)
