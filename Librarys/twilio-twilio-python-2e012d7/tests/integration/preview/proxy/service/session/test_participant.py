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


class ParticipantTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .participants(sid="KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "participant_type": "sms",
                "identifier": "identifier",
                "date_updated": "2015-07-30T20:00:00Z",
                "proxy_identifier": "proxy_identifier",
                "friendly_name": "friendly_name",
                "date_created": "2015-07-30T20:00:00Z",
                "url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "message_interactions": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessageInteractions"
                },
                "sid": "KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "session_sid": "KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .participants(sid="KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .participants.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "previous_page_url": null,
                    "next_page_url": null,
                    "url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",
                    "page": 0,
                    "first_page_url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "participants"
                },
                "participants": []
            }
            '''
        ))

        actual = self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .participants.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .participants.create(identifier="identifier")

        values = {'Identifier': "identifier"}

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "participant_type": "sms",
                "identifier": "identifier",
                "date_updated": "2015-07-30T20:00:00Z",
                "proxy_identifier": "proxy_identifier",
                "friendly_name": "friendly_name",
                "date_created": "2015-07-30T20:00:00Z",
                "url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "message_interactions": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessageInteractions"
                },
                "sid": "KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "session_sid": "KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .participants.create(identifier="identifier")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .participants(sid="KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .participants(sid="KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .participants(sid="KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "participant_type": "sms",
                "identifier": "identifier",
                "date_updated": "2015-07-30T20:00:00Z",
                "proxy_identifier": "proxy_identifier",
                "friendly_name": "friendly_name",
                "date_created": "2015-07-30T20:00:00Z",
                "url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "message_interactions": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessageInteractions"
                },
                "sid": "KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "session_sid": "KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.proxy.services(sid="KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .sessions(sid="KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .participants(sid="KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.assertIsNotNone(actual)
