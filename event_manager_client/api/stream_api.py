"""
    HighCohesion API

    HighCohesion API [https://highcohesion.co.uk](https://highcohesion.co.uk)   # noqa: E501

    The version of the OpenAPI document: 1.0.21
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
from event_manager_client.model.error_response import ErrorResponse
from event_manager_client.model.patch_sync_response import PatchSyncResponse
from event_manager_client.model.schedule_configuration import ScheduleConfiguration
from event_manager_client.model.schedule_configuration_request import ScheduleConfigurationRequest
from event_manager_client.model.sync_response import SyncResponse


class StreamApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_schedule_configuration(
            self,
            **kwargs
        ):
            """Create a new Stream Schedule Configuration  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_schedule_configuration(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                organisation_id (str): [optional]
                schedule_configuration_request (ScheduleConfigurationRequest): [optional]
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
                ScheduleConfiguration
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

        self.create_schedule_configuration = _Endpoint(
            settings={
                'response_type': (ScheduleConfiguration,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/stream/schedule_configuration',
                'operation_id': 'create_schedule_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_id',
                    'schedule_configuration_request',
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
                    'schedule_configuration_request':
                        (ScheduleConfigurationRequest,),
                },
                'attribute_map': {
                    'organisation_id': 'organisation-id',
                },
                'location_map': {
                    'organisation_id': 'header',
                    'schedule_configuration_request': 'body',
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
            callable=__create_schedule_configuration
        )

        def __delete_schedule_configuration(
            self,
            stream_id,
            **kwargs
        ):
            """Delete a Stream Schedule Configuration  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_schedule_configuration(stream_id, async_req=True)
            >>> result = thread.get()

            Args:
                stream_id (str): Stream Id

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
                SyncResponse
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
            kwargs['stream_id'] = \
                stream_id
            return self.call_with_http_info(**kwargs)

        self.delete_schedule_configuration = _Endpoint(
            settings={
                'response_type': (SyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/stream/schedule_configuration/{stream_id}',
                'operation_id': 'delete_schedule_configuration',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'stream_id',
                    'organisation_id',
                ],
                'required': [
                    'stream_id',
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
                    'stream_id':
                        (str,),
                    'organisation_id':
                        (str,),
                },
                'attribute_map': {
                    'stream_id': 'stream_id',
                    'organisation_id': 'organisation-id',
                },
                'location_map': {
                    'stream_id': 'path',
                    'organisation_id': 'header',
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
            callable=__delete_schedule_configuration
        )

        def __get_schedule_configuration(
            self,
            stream_id,
            **kwargs
        ):
            """Get a Stream Schedule Configuration by Stream Id  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_schedule_configuration(stream_id, async_req=True)
            >>> result = thread.get()

            Args:
                stream_id (str): Stream Id

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
                ScheduleConfiguration
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
            kwargs['stream_id'] = \
                stream_id
            return self.call_with_http_info(**kwargs)

        self.get_schedule_configuration = _Endpoint(
            settings={
                'response_type': (ScheduleConfiguration,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/stream/schedule_configuration/{stream_id}',
                'operation_id': 'get_schedule_configuration',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'stream_id',
                    'organisation_id',
                ],
                'required': [
                    'stream_id',
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
                    'stream_id':
                        (str,),
                    'organisation_id':
                        (str,),
                },
                'attribute_map': {
                    'stream_id': 'stream_id',
                    'organisation_id': 'organisation-id',
                },
                'location_map': {
                    'stream_id': 'path',
                    'organisation_id': 'header',
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
            callable=__get_schedule_configuration
        )

        def __update_schedule_configuration_attributes(
            self,
            **kwargs
        ):
            """Updates Stream Schedule Configuration option and active attributes.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_schedule_configuration_attributes(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                organisation_id (str): [optional]
                schedule_configuration_request (ScheduleConfigurationRequest): [optional]
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
                PatchSyncResponse
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

        self.update_schedule_configuration_attributes = _Endpoint(
            settings={
                'response_type': (PatchSyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/stream/schedule_configuration',
                'operation_id': 'update_schedule_configuration_attributes',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_id',
                    'schedule_configuration_request',
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
                    'schedule_configuration_request':
                        (ScheduleConfigurationRequest,),
                },
                'attribute_map': {
                    'organisation_id': 'organisation-id',
                },
                'location_map': {
                    'organisation_id': 'header',
                    'schedule_configuration_request': 'body',
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
            callable=__update_schedule_configuration_attributes
        )
