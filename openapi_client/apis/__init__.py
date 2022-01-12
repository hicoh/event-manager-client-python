
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
from Service.aggregate_api import AggregateApi
from Service.api_key_api import ApiKeyApi
from Service.event_api import EventApi
from Service.event_entity_api import EventEntityApi
from Service.health_api import HealthApi
from Service.job_api import JobApi
from Service.key_api import KeyApi
from Service.organisation_api import OrganisationApi
from Service.stream_api import StreamApi
from Service.webhook_api import WebhookApi
