#!/usr/bin/python

import unittest
from lib.vcs_manager import VcsManager


class doVcsManagerTests(unittest.TestCase):
  def setUp(self):
    self.manager = VcsManager()

  def test_status(self):
    result = self.manager.status('somedir')
    self.assertEqual(result, 'result')

  def test_update(self):
    result = self.manager.update('somedir')
    self.assertEqual(result, 'result')
