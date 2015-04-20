from unittest import TestCase

from slackunfuddle.transform import parse_unfuddle_changeset, unfuddle_repo

class TransformTestCase(TestCase):
    CHANGESET_XML = """<?xml version="1.0" encoding="UTF-8"?>
        <changeset>
          <author-date type="datetime">2015-04-20T11:16:27-07:00</author-date>
          <author-email>newsapps@tribune.com</author-email>
          <author-id type="integer" nil="true"></author-id>
          <author-name>Tribune News Apps</author-name>
          <committer-date type="datetime">2015-04-20T11:16:27-07:00</committer-date>
          <committer-email>newsapps@tribune.com</committer-email>
          <committer-id type="integer" nil="true"></committer-id>
          <committer-name>Tribune News Apps</committer-name>
          <created-at type="datetime">2015-04-20T11:16:28-07:00</created-at>
          <id type="integer">54138</id>
          <message>Resolving merge conflicts and merging happyhour into master</message>
          <repository-id type="integer">333</repository-id>
          <revision>4181b33ebfdcbad2bf4b0b9036a7ab4d339d7b4b</revision>
          <subdomain>tribune</subdomain>
          <branch>master</branch>
        </changeset>"""

    def test_parse_unfuddle_changeset(self):
        changeset = parse_unfuddle_changeset(self.CHANGESET_XML)
        expected = {
            'author-date': '2015-04-20T11:16:27-07:00',
            'author-email': 'newsapps@tribune.com',
            'author-id': None,
            'author-name': 'Tribune News Apps',
            'committer-date': '2015-04-20T11:16:27-07:00',
            'committer-email': 'newsapps@tribune.com',
            'committer-id': None,
            'committer-name': 'Tribune News Apps',
            'created-at': '2015-04-20T11:16:28-07:00',
            'id': '54138',
            'message': 'Resolving merge conflicts and merging happyhour into master',
            'repository-id': '333',
            'revision': '4181b33ebfdcbad2bf4b0b9036a7ab4d339d7b4b',
            'subdomain': 'tribune',
            'branch': 'master',
        }
        for k, v in expected.items():
            self.assertEqual(changeset[k], v)

    def test_unfuddle_repo(self):
        message_dict = unfuddle_repo(self.CHANGESET_XML)
        expected_text = "Tribune News Apps pushed <https://tribune.unfuddle.com/a#/repositories/333/commit?commit=4181b33ebfdcbad2bf4b0b9036a7ab4d339d7b4b|4181b> to master: Resolving merge conflicts and merging happyhour into master"
        self.assertEqual(message_dict['text'], expected_text)
