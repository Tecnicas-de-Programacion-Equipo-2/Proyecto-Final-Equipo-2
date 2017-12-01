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


class VerificationCheckTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.acc_security.services(sid="VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                            .verification_checks.create(code="code")

        values = {'Code': "code"}

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Verification/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck',
            data=values,
        ))

    def test_verification_checks_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+14159373912",
                "channel": "sms",
                "status": "approved",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z"
            }
            '''
        ))

        actual = self.client.preview.acc_security.services(sid="VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                                 .verification_checks.create(code="code")

        self.assertIsNotNone(actual)
