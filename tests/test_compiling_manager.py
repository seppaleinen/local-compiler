#!/usr/bin/python

import unittest
from lib.compiling_manager import CompilingManager


class doCompilerTests(unittest.TestCase):
  def setUp(self):
    self.manager = CompilingManager()

  def test_something(self):
    result = self.manager.guess_project_language_and_builder('somedir')
    assert result.value == 'JAVA'
