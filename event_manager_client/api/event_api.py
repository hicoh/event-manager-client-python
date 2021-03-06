"""
    HighCohesion API

    HighCohesion API [https://highcohesion.co.uk](https://highcohesion.co.uk)   # noqa: E501

    The version of the OpenAPI document: 1.0.23
    Contact: admin@highcohesion.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from event_manager_client.api_client import ApiClient, Endpoint as _Endpoint
from event_manager_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from event_manager_client.model.async_response import AsyncResponse
from event_manager_client.model.error_response import ErrorResponse
from event_manager_client.model.event import Event
from event_manager_client.model.event_list import EventList
from event_manager_client.model.redrive_event_request import RedriveEventRequest
from event_manager_client.model.replicate_event_request import ReplicateEventRequest
from event_manager_client.model.update_child_event_request import UpdateChildEventRequest
from event_manager_client.model.update_event_request import UpdateEventRequest


class EventApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_event_by_id(
            self,
            event_id,
            **kwargs
        ):
            """Get an event by event id  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_event_by_id(event_id, async_req=True)
            >>> result = thread.get()

            Args:
                event_id (str): The event id

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Event
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['event_id'] = \
                event_id
            return self.call_with_http_info(**kwargs)

        self.get_event_by_id = _Endpoint(
            settings={
                'response_type': (Event,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/event/{event_id}',
                'operation_id': 'get_event_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'event_id',
                ],
                'required': [
                    'event_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'event_id':
                        (str,),
                },
                'attribute_map': {
                    'event_id': 'event_id',
                },
                'location_map': {
                    'event_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_event_by_id
        )

        def __get_events_by(
            self,
            **kwargs
        ):
            """Get a list of events by  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_events_by(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                id (str): The event id. [optional]
                job_id (str): The job id. [optional]
                stream_id (str): The stream id. [optional]
                status (str): The status. [optional]
                limit (str): The limit (limit=20 to get the first 20 events). [optional]
                order_by (str): order by one specific field (orderBy=createdAt,desc, orderBy=status,asc). [optional]
                offset (str): the position of the first result to retrieve (offset=100). [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                EventList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_events_by = _Endpoint(
            settings={
                'response_type': (EventList,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/event',
                'operation_id': 'get_events_by',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'job_id',
                    'stream_id',
                    'status',
                    'limit',
                    'order_by',
                    'offset',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'job_id':
                        (str,),
                    'stream_id':
                        (str,),
                    'status':
                        (str,),
                    'limit':
                        (str,),
                    'order_by':
                        (str,),
                    'offset':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'job_id': 'job_id',
                    'stream_id': 'stream_id',
                    'status': 'status',
                    'limit': 'limit',
                    'order_by': 'order_by',
                    'offset': 'offset',
                },
                'location_map': {
                    'id': 'query',
                    'job_id': 'query',
                    'stream_id': 'query',
                    'status': 'query',
                    'limit': 'query',
                    'order_by': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_events_by
        )

        def __redrive_event(
            self,
            redrive_event_request,
            **kwargs
        ):
            """Redrive Event  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.redrive_event(redrive_event_request, async_req=True)
            >>> result = thread.get()

            Args:
                redrive_event_request (RedriveEventRequest): The event to redrive

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AsyncResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['redrive_event_request'] = \
                redrive_event_request
            return self.call_with_http_info(**kwargs)

        self.redrive_event = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/event/redrive',
                'operation_id': 'redrive_event',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'redrive_event_request',
                ],
                'required': [
                    'redrive_event_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'redrive_event_request':
                        (RedriveEventRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'redrive_event_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__redrive_event
        )

        def __replicate_event(
            self,
            **kwargs
        ):
            """Replicate Event  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.replicate_event(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                organisation_id (str): [optional]
                replicate_event_request (ReplicateEventRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AsyncResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.replicate_event = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/event/replicate',
                'operation_id': 'replicate_event',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_id',
                    'replicate_event_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organisation_id':
                        (str,),
                    'replicate_event_request':
                        (ReplicateEventRequest,),
                },
                'attribute_map': {
                    'organisation_id': 'organisation-id',
                },
                'location_map': {
                    'organisation_id': 'header',
                    'replicate_event_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__replicate_event
        )

        def __update_child_event(
            self,
            update_child_event_request,
            **kwargs
        ):
            """Update Child Event via the Parent Event ID and the entity name  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_child_event(update_child_event_request, async_req=True)
            >>> result = thread.get()

            Args:
                update_child_event_request (UpdateChildEventRequest): The parent ID and entity name identify the child event, the other fields will be updated on that event

            Keyword Args:
                organisation_id (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AsyncResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['update_child_event_request'] = \
                update_child_event_request
            return self.call_with_http_info(**kwargs)

        self.update_child_event = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/child_event',
                'operation_id': 'update_child_event',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'update_child_event_request',
                    'organisation_id',
                ],
                'required': [
                    'update_child_event_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'update_child_event_request':
                        (UpdateChildEventRequest,),
                    'organisation_id':
                        (str,),
                },
                'attribute_map': {
                    'organisation_id': 'organisation-id',
                },
                'location_map': {
                    'update_child_event_request': 'body',
                    'organisation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'array'
                ]
            },
            api_client=api_client,
            callable=__update_child_event
        )

        def __update_event(
            self,
            update_event_request,
            **kwargs
        ):
            """Update Event  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_event(update_event_request, async_req=True)
            >>> result = thread.get()

            Args:
                update_event_request (UpdateEventRequest): The fields to update

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AsyncResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['update_event_request'] = \
                update_event_request
            return self.call_with_http_info(**kwargs)

        self.update_event = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/event',
                'operation_id': 'update_event',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'update_event_request',
                ],
                'required': [
                    'update_event_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'update_event_request':
                        (UpdateEventRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'update_event_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'array'
                ]
            },
            api_client=api_client,
            callable=__update_event
        )
