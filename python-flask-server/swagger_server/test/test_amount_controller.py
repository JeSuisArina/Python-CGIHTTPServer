# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.expression import Expression  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAmountController(BaseTestCase):
    """AmountController integration test stubs"""

    def test_amount_post(self):
        """Test case for amount_post

        Find the sum of numbers
        """
        query_string = [('num', 56)]
        response = self.client.open(
            '/cgi-bin/cgicalc.py/amount',
            method='POST',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
