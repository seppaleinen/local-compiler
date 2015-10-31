#!/usr/bin/python

import unittest
from lib.compiling_manager import CompilingManager


class doCompilerTests(unittest.TestCase):
  def setUp(self):
    self.manager = CompilingManager()

  def test_compile_project(self):
    result = self.manager.compile_project('somedir')
    self.assertEqual(result, 'somedir')
