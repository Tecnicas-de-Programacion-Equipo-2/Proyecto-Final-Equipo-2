# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.sync.v1.service.sync_map.sync_map_item import SyncMapItemList
from twilio.rest.sync.v1.service.sync_map.sync_map_permission import SyncMapPermissionList


class SyncMapList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the SyncMapList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid

        :returns: twilio.rest.sync.v1.service.sync_map.SyncMapList
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapList
        """
        super(SyncMapList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid}
        self._uri = '/Services/{service_sid}/Maps'.format(**self._solution)

    def create(self, unique_name=values.unset, ttl=values.unset):
        """
        Create a new SyncMapInstance

        :param unicode unique_name: The unique_name
        :param unicode ttl: The ttl

        :returns: Newly created SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        """
        data = values.of({'UniqueName': unique_name, 'Ttl': ttl})

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return SyncMapInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def stream(self, limit=None, page_size=None):
        """
        Streams SyncMapInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_map.SyncMapInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'])

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncMapInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_map.SyncMapInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SyncMapInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size})

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SyncMapPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncMapInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SyncMapPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SyncMapContext

        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.sync_map.SyncMapContext
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapContext
        """
        return SyncMapContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a SyncMapContext

        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.sync_map.SyncMapContext
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapContext
        """
        return SyncMapContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncMapList>'


class SyncMapPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the SyncMapPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid

        :returns: twilio.rest.sync.v1.service.sync_map.SyncMapPage
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapPage
        """
        super(SyncMapPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncMapInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        """
        return SyncMapInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncMapPage>'


class SyncMapContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the SyncMapContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.sync_map.SyncMapContext
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapContext
        """
        super(SyncMapContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid}
        self._uri = '/Services/{service_sid}/Maps/{sid}'.format(**self._solution)

        # Dependents
        self._sync_map_items = None
        self._sync_map_permissions = None

    def fetch(self):
        """
        Fetch a SyncMapInstance

        :returns: Fetched SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SyncMapInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the SyncMapInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, ttl=values.unset):
        """
        Update the SyncMapInstance

        :param unicode ttl: The ttl

        :returns: Updated SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        """
        data = values.of({'Ttl': ttl})

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SyncMapInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    @property
    def sync_map_items(self):
        """
        Access the sync_map_items

        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_item.SyncMapItemList
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_item.SyncMapItemList
        """
        if self._sync_map_items is None:
            self._sync_map_items = SyncMapItemList(
                self._version,
                service_sid=self._solution['service_sid'],
                map_sid=self._solution['sid'],
            )
        return self._sync_map_items

    @property
    def sync_map_permissions(self):
        """
        Access the sync_map_permissions

        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionList
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionList
        """
        if self._sync_map_permissions is None:
            self._sync_map_permissions = SyncMapPermissionList(
                self._version,
                service_sid=self._solution['service_sid'],
                map_sid=self._solution['sid'],
            )
        return self._sync_map_permissions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncMapContext {}>'.format(context)


class SyncMapInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the SyncMapInstance

        :returns: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        """
        super(SyncMapInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'url': payload['url'],
            'links': payload['links'],
            'revision': payload['revision'],
            'date_expires': deserialize.iso8601_datetime(payload['date_expires']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'created_by': payload['created_by'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid']}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SyncMapContext for this SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapContext
        """
        if self._context is None:
            self._context = SyncMapContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: The unique_name
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def revision(self):
        """
        :returns: The revision
        :rtype: unicode
        """
        return self._properties['revision']

    @property
    def date_expires(self):
        """
        :returns: The date_expires
        :rtype: datetime
        """
        return self._properties['date_expires']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def created_by(self):
        """
        :returns: The created_by
        :rtype: unicode
        """
        return self._properties['created_by']

    def fetch(self):
        """
        Fetch a SyncMapInstance

        :returns: Fetched SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SyncMapInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, ttl=values.unset):
        """
        Update the SyncMapInstance

        :param unicode ttl: The ttl

        :returns: Updated SyncMapInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.SyncMapInstance
        """
        return self._proxy.update(ttl=ttl)

    @property
    def sync_map_items(self):
        """
        Access the sync_map_items

        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_item.SyncMapItemList
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_item.SyncMapItemList
        """
        return self._proxy.sync_map_items

    @property
    def sync_map_permissions(self):
        """
        Access the sync_map_permissions

        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionList
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionList
        """
        return self._proxy.sync_map_permissions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncMapInstance {}>'.format(context)
