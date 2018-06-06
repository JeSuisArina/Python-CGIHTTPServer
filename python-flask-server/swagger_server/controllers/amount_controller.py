import connexion
import six

from swagger_server.models.expression import Expression  # noqa: E501
from swagger_server import util


def amount_post(num):  # noqa: E501
	"""Find the sum of numbers

	# noqa: E501

	:param num: Add a number to the expression
	:type num: List[int]

	:rtype: Expression
	"""

	result = ""
	res = 0
	for i in range(len(num)-1):
		res = res + int(num[i])
		result = result + str(num[i]) + "+"
	res = res + int(num[-1])
	result = result + str(num[-1]) + "=" + str(res)
	return result
