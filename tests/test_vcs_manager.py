#!/usr/bin/python

import unittest
import mock
import os
from lib.vcs_manager import VcsManager


class VcsManager_status(unittest.TestCase):
  def setUp(self):
    self.manager = VcsManager()

  @mock.patch('lib.vcs_manager.subprocess')
  def test_status(self, mocked):
    base_dir = os.getcwd()
    git_dir = os.path.join(base_dir, '.git')

    result = self.manager.status(base_dir)

    mocked.Popen.assert_called_with([
      'git', 
      '--work-tree=' + base_dir, 
      '--git-dir=' + git_dir, 
      'status'], 
      stdout=mocked.PIPE)


class VcsManager_update(unittest.TestCase):
  def setUp(self):
    self.manager = VcsManager()

  @mock.patch('lib.vcs_manager.subprocess')
  def test_update(self, mocked):
    base_dir = os.getcwd()
    git_dir = os.path.join(base_dir, '.git')

    result = self.manager.update(base_dir)

    mocked.Popen.assert_called_with([
      'git', 
      '--work-tree=' + base_dir, 
      '--git-dir=' + git_dir, 
      'pull'], 
      stdout=mocked.PIPE)
