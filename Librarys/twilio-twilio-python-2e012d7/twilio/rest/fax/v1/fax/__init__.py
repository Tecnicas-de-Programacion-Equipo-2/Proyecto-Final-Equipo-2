# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.fax.v1.fax.fax_media import FaxMediaList


class FaxList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the FaxList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.fax.v1.fax.FaxList
        :rtype: twilio.rest.fax.v1.fax.FaxList
        """
        super(FaxList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Faxes'.format(**self._solution)

    def stream(self, from_=values.unset, to=values.unset,
               date_created_on_or_before=values.unset,
               date_created_after=values.unset, limit=None, page_size=None):
        """
        Streams FaxInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode from_: Include only faxes sent from
        :param unicode to: Include only faxes sent to
        :param datetime date_created_on_or_before: Include only faxes created on or before
        :param datetime date_created_after: Include only faxes created after
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.fax.v1.fax.FaxInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            from_=from_,
            to=to,
            date_created_on_or_before=date_created_on_or_before,
            date_created_after=date_created_after,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, from_=values.unset, to=values.unset,
             date_created_on_or_before=values.unset,
             date_created_after=values.unset, limit=None, page_size=None):
        """
        Lists FaxInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode from_: Include only faxes sent from
        :param unicode to: Include only faxes sent to
        :param datetime date_created_on_or_before: Include only faxes created on or before
        :param datetime date_created_after: Include only faxes created after
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.fax.v1.fax.FaxInstance]
        """
        return list(self.stream(
            from_=from_,
            to=to,
            date_created_on_or_before=date_created_on_or_before,
            date_created_after=date_created_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, from_=values.unset, to=values.unset,
             date_created_on_or_before=values.unset,
             date_created_after=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FaxInstance records from the API.
        Request is executed immediately

        :param unicode from_: Include only faxes sent from
        :param unicode to: Include only faxes sent to
        :param datetime date_created_on_or_before: Include only faxes created on or before
        :param datetime date_created_after: Include only faxes created after
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxPage
        """
        params = values.of({
            'From': from_,
            'To': to,
            'DateCreatedOnOrBefore': serialize.iso8601_datetime(date_created_on_or_before),
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return FaxPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FaxInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FaxPage(self._version, response, self._solution)

    def create(self, to, media_url, quality=values.unset,
               status_callback=values.unset, from_=values.unset,
               sip_auth_username=values.unset, sip_auth_password=values.unset,
               store_media=values.unset):
        """
        Create a new FaxInstance

        :param unicode to: The phone number or SIP address to send the fax to
        :param unicode media_url: URL that points to the fax media
        :param FaxInstance.Quality quality: The quality of this fax
        :param unicode status_callback: URL for fax status callbacks
        :param unicode from_: Twilio number from which to originate the fax
        :param unicode sip_auth_username: Username for SIP authentication
        :param unicode sip_auth_password: Password for SIP authentication
        :param bool store_media: Whether or not to store media

        :returns: Newly created FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxInstance
        """
        data = values.of({
            'To': to,
            'MediaUrl': media_url,
            'Quality': quality,
            'StatusCallback': status_callback,
            'From': from_,
            'SipAuthUsername': sip_auth_username,
            'SipAuthPassword': sip_auth_password,
            'StoreMedia': store_media,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return FaxInstance(self._version, payload)

    def get(self, sid):
        """
        Constructs a FaxContext

        :param sid: A string that uniquely identifies this fax.

        :returns: twilio.rest.fax.v1.fax.FaxContext
        :rtype: twilio.rest.fax.v1.fax.FaxContext
        """
        return FaxContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a FaxContext

        :param sid: A string that uniquely identifies this fax.

        :returns: twilio.rest.fax.v1.fax.FaxContext
        :rtype: twilio.rest.fax.v1.fax.FaxContext
        """
        return FaxContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Fax.V1.FaxList>'


class FaxPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the FaxPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.fax.v1.fax.FaxPage
        :rtype: twilio.rest.fax.v1.fax.FaxPage
        """
        super(FaxPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FaxInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.fax.v1.fax.FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxInstance
        """
        return FaxInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Fax.V1.FaxPage>'


class FaxContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, sid):
        """
        Initialize the FaxContext

        :param Version version: Version that contains the resource
        :param sid: A string that uniquely identifies this fax.

        :returns: twilio.rest.fax.v1.fax.FaxContext
        :rtype: twilio.rest.fax.v1.fax.FaxContext
        """
        super(FaxContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid}
        self._uri = '/Faxes/{sid}'.format(**self._solution)

        # Dependents
        self._media = None

    def fetch(self):
        """
        Fetch a FaxInstance

        :returns: Fetched FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return FaxInstance(self._version, payload, sid=self._solution['sid'])

    def update(self, status=values.unset):
        """
        Update the FaxInstance

        :param FaxInstance.UpdateStatus status: The updated status of this fax

        :returns: Updated FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxInstance
        """
        data = values.of({'Status': status})

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return FaxInstance(self._version, payload, sid=self._solution['sid'])

    def delete(self):
        """
        Deletes the FaxInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def media(self):
        """
        Access the media

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaList
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaList
        """
        if self._media is None:
            self._media = FaxMediaList(self._version, fax_sid=self._solution['sid'])
        return self._media

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Fax.V1.FaxContext {}>'.format(context)


class FaxInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Direction(object):
        INBOUND = "inbound"
        OUTBOUND = "outbound"

    class Quality(object):
        STANDARD = "standard"
        FINE = "fine"
        SUPERFINE = "superfine"

    class Status(object):
        QUEUED = "queued"
        PROCESSING = "processing"
        SENDING = "sending"
        DELIVERED = "delivered"
        RECEIVING = "receiving"
        RECEIVED = "received"
        NO_ANSWER = "no-answer"
        BUSY = "busy"
        FAILED = "failed"
        CANCELED = "canceled"

    class UpdateStatus(object):
        CANCELED = "canceled"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the FaxInstance

        :returns: twilio.rest.fax.v1.fax.FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxInstance
        """
        super(FaxInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'from_': payload['from'],
            'to': payload['to'],
            'quality': payload['quality'],
            'media_sid': payload['media_sid'],
            'media_url': payload['media_url'],
            'num_pages': deserialize.integer(payload['num_pages']),
            'duration': deserialize.integer(payload['duration']),
            'status': payload['status'],
            'direction': payload['direction'],
            'api_version': payload['api_version'],
            'price': deserialize.decimal(payload['price']),
            'price_unit': payload['price_unit'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'links': payload['links'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid']}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FaxContext for this FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxContext
        """
        if self._context is None:
            self._context = FaxContext(self._version, sid=self._solution['sid'])
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this fax.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account SID
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def from_(self):
        """
        :returns: The party that sent the fax
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def to(self):
        """
        :returns: The party that received the fax
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def quality(self):
        """
        :returns: The quality of this fax
        :rtype: FaxInstance.Quality
        """
        return self._properties['quality']

    @property
    def media_sid(self):
        """
        :returns: Media SID
        :rtype: unicode
        """
        return self._properties['media_sid']

    @property
    def media_url(self):
        """
        :returns: URL pointing to fax media
        :rtype: unicode
        """
        return self._properties['media_url']

    @property
    def num_pages(self):
        """
        :returns: Number of pages
        :rtype: unicode
        """
        return self._properties['num_pages']

    @property
    def duration(self):
        """
        :returns: The time taken to transmit the fax
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def status(self):
        """
        :returns: The status of this fax
        :rtype: FaxInstance.Status
        """
        return self._properties['status']

    @property
    def direction(self):
        """
        :returns: The direction of this fax
        :rtype: FaxInstance.Direction
        """
        return self._properties['direction']

    @property
    def api_version(self):
        """
        :returns: The API version used
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def price(self):
        """
        :returns: Fax transmission price
        :rtype: unicode
        """
        return self._properties['price']

    @property
    def price_unit(self):
        """
        :returns: Currency used for billing
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def date_created(self):
        """
        :returns: The date this fax was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this fax was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def links(self):
        """
        :returns: Nested resource URLs
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def url(self):
        """
        :returns: The URL of this resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a FaxInstance

        :returns: Fetched FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxInstance
        """
        return self._proxy.fetch()

    def update(self, status=values.unset):
        """
        Update the FaxInstance

        :param FaxInstance.UpdateStatus status: The updated status of this fax

        :returns: Updated FaxInstance
        :rtype: twilio.rest.fax.v1.fax.FaxInstance
        """
        return self._proxy.update(status=status)

    def delete(self):
        """
        Deletes the FaxInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def media(self):
        """
        Access the media

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaList
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaList
        """
        return self._proxy.media

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Fax.V1.FaxInstance {}>'.format(context)
