"""
    HighCohesion API

    HighCohesion API [https://highcohesion.co.uk](https://highcohesion.co.uk)   # noqa: E501

    The version of the OpenAPI document: 1.0.21
    Contact: admin@highcohesion.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.async_response import AsyncResponse
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.job import Job
from openapi_client.model.job_list import JobList
from openapi_client.model.job_request import JobRequest
from openapi_client.model.job_schedule_request import JobScheduleRequest
from openapi_client.model.replicate_job_request import ReplicateJobRequest
from openapi_client.model.sync_response import SyncResponse
from openapi_client.model.update_job_request import UpdateJobRequest


class JobApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_job(
            self,
            **kwargs
        ):
            """Create a new job  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_job(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                job_request (JobRequest): [optional]
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

        self.create_job = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/job',
                'operation_id': 'create_job',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'job_request',
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
                    'job_request':
                        (JobRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'job_request': 'body',
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
            callable=__create_job
        )

        def __create_job_schedule(
            self,
            **kwargs
        ):
            """Create a job schedule  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_job_schedule(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                organisation_id (str): [optional]
                job_schedule_request (JobScheduleRequest): [optional]
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

        self.create_job_schedule = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/job/schedule',
                'operation_id': 'create_job_schedule',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_id',
                    'job_schedule_request',
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
                    'job_schedule_request':
                        (JobScheduleRequest,),
                },
                'attribute_map': {
                    'organisation_id': 'organisation-id',
                },
                'location_map': {
                    'organisation_id': 'header',
                    'job_schedule_request': 'body',
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
            callable=__create_job_schedule
        )

        def __delete_job(
            self,
            **kwargs
        ):
            """Delete jobs  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_job(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                organisation_id (str): [optional]
                id (str): The job id. [optional]
                stream_id (str): The stream id of the job. [optional]
                status (str): The job status. [optional]
                due_at (str): Delete jobs filtered by due_at date (due_at=2021/03/21 12:23:22,gte). [optional]
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
            return self.call_with_http_info(**kwargs)

        self.delete_job = _Endpoint(
            settings={
                'response_type': (SyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/job',
                'operation_id': 'delete_job',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_id',
                    'id',
                    'stream_id',
                    'status',
                    'due_at',
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
                    'id':
                        (str,),
                    'stream_id':
                        (str,),
                    'status':
                        (str,),
                    'due_at':
                        (str,),
                },
                'attribute_map': {
                    'organisation_id': 'organisation-id',
                    'id': 'id',
                    'stream_id': 'stream_id',
                    'status': 'status',
                    'due_at': 'due_at',
                },
                'location_map': {
                    'organisation_id': 'header',
                    'id': 'query',
                    'stream_id': 'query',
                    'status': 'query',
                    'due_at': 'query',
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
            callable=__delete_job
        )

        def __get_job_by_id(
            self,
            job_id,
            **kwargs
        ):
            """Get a job by job id  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_job_by_id(job_id, async_req=True)
            >>> result = thread.get()

            Args:
                job_id (str): The job id

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
                Job
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
            kwargs['job_id'] = \
                job_id
            return self.call_with_http_info(**kwargs)

        self.get_job_by_id = _Endpoint(
            settings={
                'response_type': (Job,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/job/{job_id}',
                'operation_id': 'get_job_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'job_id',
                ],
                'required': [
                    'job_id',
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
                    'job_id':
                        (str,),
                },
                'attribute_map': {
                    'job_id': 'job_id',
                },
                'location_map': {
                    'job_id': 'path',
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
            callable=__get_job_by_id
        )

        def __get_jobs_by(
            self,
            **kwargs
        ):
            """Get a list of jobs by  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_jobs_by(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                id (str): The job id. [optional]
                stream_id (str): The stream id of the job. [optional]
                status (str): The job status. [optional]
                limit (str): The limit (limit=20 to get the first 20 jobs). [optional]
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
                JobList
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

        self.get_jobs_by = _Endpoint(
            settings={
                'response_type': (JobList,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/job',
                'operation_id': 'get_jobs_by',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
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
                    'stream_id': 'stream_id',
                    'status': 'status',
                    'limit': 'limit',
                    'order_by': 'order_by',
                    'offset': 'offset',
                },
                'location_map': {
                    'id': 'query',
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
            callable=__get_jobs_by
        )

        def __replicate_job(
            self,
            **kwargs
        ):
            """Replicate job  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.replicate_job(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                replicate_job_request (ReplicateJobRequest): [optional]
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

        self.replicate_job = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/job/replicate',
                'operation_id': 'replicate_job',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'replicate_job_request',
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
                    'replicate_job_request':
                        (ReplicateJobRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'replicate_job_request': 'body',
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
            callable=__replicate_job
        )

        def __update_job(
            self,
            update_job_request,
            **kwargs
        ):
            """Update job  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_job(update_job_request, async_req=True)
            >>> result = thread.get()

            Args:
                update_job_request (UpdateJobRequest): The fields to update

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
            kwargs['update_job_request'] = \
                update_job_request
            return self.call_with_http_info(**kwargs)

        self.update_job = _Endpoint(
            settings={
                'response_type': (AsyncResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/event_manager/job',
                'operation_id': 'update_job',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'update_job_request',
                ],
                'required': [
                    'update_job_request',
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
                    'update_job_request':
                        (UpdateJobRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'update_job_request': 'body',
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
            callable=__update_job
        )
