#!/usr/bin/python

import unittest
from lib.project_type_manager import ProjectTypeManager


class doProjectTypeTests(unittest.TestCase):
  def setUp(self):
    self.manager = ProjectTypeManager()

  def test_guess_language(self):
    result = self.manager.guess_language('somedir')
    assert result.value == 'JAVA'

  def test_guess_buildtool(self):
    result = self.manager.guess_buildtool('somedir')
    assert result.value == 'MAVEN'
