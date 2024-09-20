from module.helpers import print_string

class Module:
	def __init__(self, test_str: str) -> None:
		"""Initiating the Module class

		Args:
			test_str (str): What to pass to the helper function test (print)
		"""
		print_string(test_str)
	
	def __str__(self) -> str:
		"""Prints the test string

		Returns:
			str: Test string from __init__ func
		"""
		return self.test_str