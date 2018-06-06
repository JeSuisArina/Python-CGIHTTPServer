import connexion
import six

from swagger_server.models.expression import Expression  # noqa: E501
from swagger_server import util


def division_post(num):  # noqa: E501
    """Find the result of dividing the numbers

     # noqa: E501

    :param num: Add a number to the expression
    :type num: List[int]

    :rtype: Expression
    """
    return 'do some magic!'
