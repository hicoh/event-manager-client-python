
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.aggregate_api import AggregateApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from event_manager_client.api.aggregate_api import AggregateApi
from event_manager_client.api.api_key_api import ApiKeyApi
from event_manager_client.api.event_api import EventApi
from event_manager_client.api.event_entity_api import EventEntityApi
from event_manager_client.api.health_api import HealthApi
from event_manager_client.api.job_api import JobApi
from event_manager_client.api.key_api import KeyApi
from event_manager_client.api.organisation_api import OrganisationApi
from event_manager_client.api.stream_api import StreamApi
from event_manager_client.api.webhook_api import WebhookApi
