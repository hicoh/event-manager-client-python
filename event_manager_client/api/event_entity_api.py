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
from event_manager_client.model.update_event_entity_request import UpdateEventEntityRequest


class EventEntityApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __update_event_entity(
            self,
            update_event_entity_request,
            **kwargs
        ):
            """Update Event Entity  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_event_entity(update_event_entity_request, async_req=True)
            >>> result = thread.get()

            Args:
                update_event_entity_request (UpdateEventEntityRequest): The fields to update

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
            kwargs['update_event_entity_request'] = \
                update_event_entity_request
            return self.call_with_http_info(**kwargs)

        self.update_event_entity = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/event_entity',
                'operation_id': 'update_event_entity',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'update_event_entity_request',
                ],
                'required': [
                    'update_event_entity_request',
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
                    'update_event_entity_request':
                        (UpdateEventEntityRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'update_event_entity_request': 'body',
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
            callable=__update_event_entity
        )
