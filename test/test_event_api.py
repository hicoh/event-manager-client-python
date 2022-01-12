"""
    HighCohesion API

    HighCohesion API [https://highcohesion.co.uk](https://highcohesion.co.uk)   # noqa: E501

    The version of the OpenAPI document: 1.0.21
    Contact: admin@highcohesion.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from Service.event_api import EventApi  # noqa: E501


class TestEventApi(unittest.TestCase):
    """EventApi unit test stubs"""

    def setUp(self):
        self.api = EventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_event_by_id(self):
        """Test case for get_event_by_id

        Get an event by event id  # noqa: E501
        """
        pass

    def test_get_events_by(self):
        """Test case for get_events_by

        Get a list of events by  # noqa: E501
        """
        pass

    def test_redrive_event(self):
        """Test case for redrive_event

        Redrive Event  # noqa: E501
        """
        pass

    def test_replicate_event(self):
        """Test case for replicate_event

        Replicate Event  # noqa: E501
        """
        pass

    def test_update_child_event(self):
        """Test case for update_child_event

        Update Child Event via the Parent Event ID and the entity name  # noqa: E501
        """
        pass

    def test_update_event(self):
        """Test case for update_event

        Update Event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
