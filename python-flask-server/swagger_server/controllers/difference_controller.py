import connexion
import six

from swagger_server.models.expression import Expression  # noqa: E501
from swagger_server import util


def difference_post(num):  # noqa: E501
    """Find the difference of numbers

     # noqa: E501

    :param num: Add a number to the expression
    :type num: List[int]

    :rtype: Expression
    """
    return 'do some magic!'
