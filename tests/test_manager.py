#!/usr/bin/python

import unittest, mock, sys
from lib.manager import Manager

class doCompilerTests(unittest.TestCase):
	def setUp(self):
		self.manager = Manager()

	def test_one(self):
		mock_stdout = mock.Mock()
		sys.stdout = mock_stdout
	
		result = self.manager.method('value')

		sys.stdout = sys.__stdout__

		expected = []
		expected.append(mock.call.write('value'))
		expected.append(mock.call.write('\n'))

		assert expected == mock_stdout.mock_calls

		assert result == 'value'
