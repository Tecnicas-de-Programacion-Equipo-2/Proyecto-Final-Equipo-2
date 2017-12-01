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


class RatePlanTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.rate_plans.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://wireless.twilio.com/v1/RatePlans',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/RatePlans?PageSize=50&Page=0",
                    "key": "rate_plans",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/RatePlans?PageSize=50&Page=0"
                },
                "rate_plans": []
            }
            '''
        ))

        actual = self.client.wireless.v1.rate_plans.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/RatePlans?PageSize=50&Page=0",
                    "key": "rate_plans",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/RatePlans?PageSize=50&Page=0"
                },
                "rate_plans": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "unique_name",
                        "data_enabled": true,
                        "data_limit": 1000,
                        "data_metering": "pooled",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "friendly_name": "friendly_name",
                        "messaging_enabled": true,
                        "voice_enabled": true,
                        "national_roaming_enabled": true,
                        "national_roaming_data_limit": 1000,
                        "international_roaming": [
                            "data",
                            "messaging",
                            "voice"
                        ],
                        "international_roaming_data_limit": 1000,
                        "sid": "WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.wireless.v1.rate_plans.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.rate_plans(sid="WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "data_enabled": true,
                "data_limit": 1000,
                "data_metering": "pooled",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "messaging_enabled": true,
                "voice_enabled": true,
                "national_roaming_enabled": true,
                "national_roaming_data_limit": 1000,
                "international_roaming": [
                    "data",
                    "messaging",
                    "voice"
                ],
                "international_roaming_data_limit": 1000,
                "sid": "WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.wireless.v1.rate_plans(sid="WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.rate_plans.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://wireless.twilio.com/v1/RatePlans',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "data_enabled": true,
                "data_limit": 1000,
                "data_metering": "pooled",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "messaging_enabled": true,
                "voice_enabled": true,
                "national_roaming_enabled": true,
                "national_roaming_data_limit": 1000,
                "international_roaming": [
                    "data",
                    "messaging",
                    "voice"
                ],
                "international_roaming_data_limit": 1000,
                "sid": "WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.wireless.v1.rate_plans.create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.rate_plans(sid="WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "data_enabled": true,
                "data_limit": 1000,
                "data_metering": "pooled",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "messaging_enabled": true,
                "voice_enabled": true,
                "national_roaming_enabled": true,
                "national_roaming_data_limit": 1000,
                "international_roaming": [
                    "data",
                    "messaging",
                    "voice"
                ],
                "international_roaming_data_limit": 1000,
                "sid": "WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.wireless.v1.rate_plans(sid="WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.rate_plans(sid="WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.wireless.v1.rate_plans(sid="WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)
