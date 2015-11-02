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

    result = self.manager.status(base_dir)

    mocked.Popen.assert_called_with([
      'git', 
      '--work-tree=/Users/seppa/Workspace/local-compiler', 
      '--git-dir=/Users/seppa/Workspace/local-compiler/.git', 
      'status'], 
      stdout=mocked.PIPE)


class VcsManager_update(unittest.TestCase):
  def setUp(self):
    self.manager = VcsManager()

  @mock.patch('lib.vcs_manager.subprocess')
  def test_update(self, mocked):
    base_dir = os.getcwd()

    result = self.manager.update(base_dir)

    mocked.Popen.assert_called_with([
      'git', 
      '--work-tree=/Users/seppa/Workspace/local-compiler', 
      '--git-dir=/Users/seppa/Workspace/local-compiler/.git', 
      'pull'], 
      stdout=mocked.PIPE)
