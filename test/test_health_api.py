"""
    HighCohesion API

    HighCohesion API [https://highcohesion.co.uk](https://highcohesion.co.uk)   # noqa: E501

    The version of the OpenAPI document: 1.0.21
    Contact: admin@highcohesion.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from Service.health_api import HealthApi  # noqa: E501


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_health(self):
        """Test case for get_health

        Get Health  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
