# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.expression_result import ExpressionResult  # noqa: F401,E501
from swagger_server import util


class Expression(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, num: List[int]=None, result: ExpressionResult=None):  # noqa: E501
        """Expression - a model defined in Swagger

        :param num: The num of this Expression.  # noqa: E501
        :type num: List[int]
        :param result: The result of this Expression.  # noqa: E501
        :type result: ExpressionResult
        """
        self.swagger_types = {
            'num': List[int],
            'result': ExpressionResult
        }

        self.attribute_map = {
            'num': 'num',
            'result': 'result'
        }

        self._num = num
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'Expression':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Expression of this Expression.  # noqa: E501
        :rtype: Expression
        """
        return util.deserialize_model(dikt, cls)

    @property
    def num(self) -> List[int]:
        """Gets the num of this Expression.


        :return: The num of this Expression.
        :rtype: List[int]
        """
        return self._num

    @num.setter
    def num(self, num: List[int]):
        """Sets the num of this Expression.


        :param num: The num of this Expression.
        :type num: List[int]
        """

        self._num = num

    @property
    def result(self) -> ExpressionResult:
        """Gets the result of this Expression.


        :return: The result of this Expression.
        :rtype: ExpressionResult
        """
        return self._result

    @result.setter
    def result(self, result: ExpressionResult):
        """Sets the result of this Expression.


        :param result: The result of this Expression.
        :type result: ExpressionResult
        """

        self._result = result
