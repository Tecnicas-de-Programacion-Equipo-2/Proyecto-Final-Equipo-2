# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class UsageTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.wireless.sims(sid="DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .usage().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/wireless/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "commands_costs": {},
                "commands_usage": {},
                "data_costs": {},
                "data_usage": {},
                "sim_unique_name": "sim_unique_name",
                "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "period": {},
                "url": "https://preview.twilio.com/wireless/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage"
            }
            '''
        ))

        actual = self.client.preview.wireless.sims(sid="DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                             .usage().fetch()

        self.assertIsNotNone(actual)
