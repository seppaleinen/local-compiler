#!/usr/bin/python

import unittest
from lib.manager import Manager

class doCompilerTests(unittest.TestCase):
	def setUp(self):
		self.manager = Manager()

	def test_one(self):
		result = self.manager.method('value')
		assert result == 'value'
