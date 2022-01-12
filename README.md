# event-manager-client-python
HighCohesion API
[https://highcohesion.co.uk](https://highcohesion.co.uk)


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.23
- Package version: 1.0.23
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/hicoh/event-manager-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/hicoh/event-manager-client-python.git`)

Then import the package:
```python
import event_manager_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import event_manager_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import event_manager_client
from pprint import pprint
from event_manager_client.api import aggregate_api
from event_manager_client.model.async_response import AsyncResponse
from event_manager_client.model.replicate_event_request import ReplicateEventRequest
from event_manager_client.model.replicate_parent_aggregate_event_request import ReplicateParentAggregateEventRequest
# Defining the host is optional and defaults to https://api.highcohesion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = event_manager_client.Configuration(
    host = "https://api.highcohesion.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: admin_apikey
configuration.api_key['admin_apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['admin_apikey'] = 'Bearer'


# Enter a context with an instance of the API client
with event_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aggregate_api.AggregateApi(api_client)
    organisation_id = "123e4567-e89b-12d3-a456-426614174000" # str | 
stream_id = "123e4567-e89b-12d3-a456-426614174000" # str | 
job_id = "123e4567-e89b-12d3-a456-426614174000" # str | 

    try:
        # Aggregate all events from a specific job
        api_response = api_instance.get_aggregate_events(organisation_id, stream_id, job_id)
        pprint(api_response)
    except event_manager_client.ApiException as e:
        print("Exception when calling AggregateApi->get_aggregate_events: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.highcohesion.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AggregateApi* | [**get_aggregate_events**](docs/AggregateApi.md#get_aggregate_events) | **GET** /event_manager/aggregate_events/{organisation_id}/{stream_id}/{job_id} | Aggregate all events from a specific job
*AggregateApi* | [**replicate_child_aggregate_event**](docs/AggregateApi.md#replicate_child_aggregate_event) | **POST** /event_manager/aggregate_events/replicate_child | Replicate Child Aggregate Event
*AggregateApi* | [**replicate_parent_aggregate_event**](docs/AggregateApi.md#replicate_parent_aggregate_event) | **POST** /event_manager/aggregate_events/replicate_parent | Replicate a Parent Aggregate event
*ApiKeyApi* | [**create_api_key**](docs/ApiKeyApi.md#create_api_key) | **POST** /event_manager/api_key | Create a new API key
*ApiKeyApi* | [**delete_api_key**](docs/ApiKeyApi.md#delete_api_key) | **DELETE** /event_manager/api_key/{organisation_id}/{key_id} | Delete an API key
*ApiKeyApi* | [**get_all_api_keys_by_organisation**](docs/ApiKeyApi.md#get_all_api_keys_by_organisation) | **GET** /event_manager/api_key/all/organisation/{organisation_id} | Fetch all API keys associated with an Organisation
*EventApi* | [**get_event_by_id**](docs/EventApi.md#get_event_by_id) | **GET** /event_manager/event/{event_id} | Get an event by event id
*EventApi* | [**get_events_by**](docs/EventApi.md#get_events_by) | **GET** /event_manager/event | Get a list of events by
*EventApi* | [**redrive_event**](docs/EventApi.md#redrive_event) | **POST** /event_manager/event/redrive | Redrive Event
*EventApi* | [**replicate_event**](docs/EventApi.md#replicate_event) | **POST** /event_manager/event/replicate | Replicate Event
*EventApi* | [**update_child_event**](docs/EventApi.md#update_child_event) | **PATCH** /event_manager/child_event | Update Child Event via the Parent Event ID and the entity name
*EventApi* | [**update_event**](docs/EventApi.md#update_event) | **PATCH** /event_manager/event | Update Event
*EventEntityApi* | [**update_event_entity**](docs/EventEntityApi.md#update_event_entity) | **PATCH** /event_manager/event_entity | Update Event Entity
*HealthApi* | [**get_health**](docs/HealthApi.md#get_health) | **GET** /event_manager/health | Get Health
*JobApi* | [**create_job**](docs/JobApi.md#create_job) | **POST** /event_manager/job | Create a new job
*JobApi* | [**create_job_schedule**](docs/JobApi.md#create_job_schedule) | **POST** /event_manager/job/schedule | Create a job schedule
*JobApi* | [**create_source_job**](docs/JobApi.md#create_source_job) | **POST** /event_manager/job/source | Trigger a job to be sent to the source
*JobApi* | [**delete_job**](docs/JobApi.md#delete_job) | **DELETE** /event_manager/job | Delete jobs
*JobApi* | [**get_job_by_id**](docs/JobApi.md#get_job_by_id) | **GET** /event_manager/job/{job_id} | Get a job by job id
*JobApi* | [**get_jobs_by**](docs/JobApi.md#get_jobs_by) | **GET** /event_manager/job | Get a list of jobs by
*JobApi* | [**replicate_job**](docs/JobApi.md#replicate_job) | **POST** /event_manager/job/replicate | Replicate job
*JobApi* | [**update_job**](docs/JobApi.md#update_job) | **PATCH** /event_manager/job | Update job
*KeyApi* | [**get_key**](docs/KeyApi.md#get_key) | **GET** /event_manager/key/{id} | Fetch key
*OrganisationApi* | [**create_organisation_index**](docs/OrganisationApi.md#create_organisation_index) | **POST** /event_manager/organisation/{organisation_id}/index | Create the organisation tables
*StreamApi* | [**create_schedule_configuration**](docs/StreamApi.md#create_schedule_configuration) | **POST** /event_manager/stream/schedule_configuration | Create a new Stream Schedule Configuration
*StreamApi* | [**delete_schedule_configuration**](docs/StreamApi.md#delete_schedule_configuration) | **DELETE** /event_manager/stream/schedule_configuration/{stream_id} | Delete a Stream Schedule Configuration
*StreamApi* | [**get_schedule_configuration**](docs/StreamApi.md#get_schedule_configuration) | **GET** /event_manager/stream/schedule_configuration/{stream_id} | Get a Stream Schedule Configuration by Stream Id
*StreamApi* | [**update_schedule_configuration_attributes**](docs/StreamApi.md#update_schedule_configuration_attributes) | **PATCH** /event_manager/stream/schedule_configuration | Updates Stream Schedule Configuration option and active attributes.
*WebhookApi* | [**post_dynamic_webhook**](docs/WebhookApi.md#post_dynamic_webhook) | **POST** /event_manager/webhook/dynamic/{stream_id} | Dynamic Webhook
*WebhookApi* | [**post_static_webhook**](docs/WebhookApi.md#post_static_webhook) | **POST** /event_manager/webhook/static/{stream_id} | Static Webhook
*WebhookApi* | [**replicate_dynamic_webhook**](docs/WebhookApi.md#replicate_dynamic_webhook) | **POST** /event_manager/job/replicate/webhook/dynamic | Replicate Dynamic Webhook
*WebhookApi* | [**replicate_static_webhook**](docs/WebhookApi.md#replicate_static_webhook) | **POST** /event_manager/job/replicate/webhook/static | Replicate Static Webhook


## Documentation For Models

 - [ApiKeyList](docs/ApiKeyList.md)
 - [ApiKeyRequest](docs/ApiKeyRequest.md)
 - [ApiKeyResponse](docs/ApiKeyResponse.md)
 - [AsyncResponse](docs/AsyncResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Event](docs/Event.md)
 - [EventList](docs/EventList.md)
 - [FullApiKey](docs/FullApiKey.md)
 - [Health](docs/Health.md)
 - [Job](docs/Job.md)
 - [JobList](docs/JobList.md)
 - [JobRequest](docs/JobRequest.md)
 - [JobScheduleRequest](docs/JobScheduleRequest.md)
 - [PatchSyncResponse](docs/PatchSyncResponse.md)
 - [PayloadInList](docs/PayloadInList.md)
 - [RedriveEventRequest](docs/RedriveEventRequest.md)
 - [ReplicateEventRequest](docs/ReplicateEventRequest.md)
 - [ReplicateJobRequest](docs/ReplicateJobRequest.md)
 - [ReplicateParentAggregateEventRequest](docs/ReplicateParentAggregateEventRequest.md)
 - [ReplicateWebhook](docs/ReplicateWebhook.md)
 - [ScheduleConfiguration](docs/ScheduleConfiguration.md)
 - [ScheduleConfigurationRequest](docs/ScheduleConfigurationRequest.md)
 - [SourceJobRequest](docs/SourceJobRequest.md)
 - [SyncResponse](docs/SyncResponse.md)
 - [UpdateChildEventRequest](docs/UpdateChildEventRequest.md)
 - [UpdateEventEntityRequest](docs/UpdateEventEntityRequest.md)
 - [UpdateEventRequest](docs/UpdateEventRequest.md)
 - [UpdateJobRequest](docs/UpdateJobRequest.md)


## Documentation For Authorization


## admin_apikey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: HTTP header


## apikey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: HTTP header


## Author

admin@highcohesion.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in event_manager_client.apis and event_manager_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from event_manager_client.api.default_api import DefaultApi`
- `from event_manager_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import event_manager_client
from event_manager_client.apis import *
from event_manager_client.models import *
```

