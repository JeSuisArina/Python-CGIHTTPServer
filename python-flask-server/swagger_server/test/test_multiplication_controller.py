# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.expression import Expression  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMultiplicationController(BaseTestCase):
    """MultiplicationController integration test stubs"""

    def test_multiplication_post(self):
        """Test case for multiplication_post

        Find the multiplication of numbers
        """
        query_string = [('num', 56)]
        response = self.client.open(
            '/cgi-bin/cgicalc.py/multiplication',
            method='POST',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
