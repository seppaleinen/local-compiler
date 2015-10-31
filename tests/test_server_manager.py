#!/usr/bin/python

import unittest
from lib.server_manager import ServerManager
from lib.model.enums import ServerDeployStatus, ServerStatus


class doServerManager_direct_deploy_to_serverTests(unittest.TestCase):
  def setUp(self):
    self.manager = ServerManager()

  def test_direct_deploy_to_server_somedir(self):
    result = self.manager.direct_deploy_to_server('somedir')
    self.assertEqual(result, ServerDeployStatus.SUCCESS)

  def test_direct_deploy_to_server_otherdir(self):
    result = self.manager.direct_deploy_to_server('otherdir')
    self.assertEqual(result, ServerDeployStatus.FAILURE)


class doServerManager_remote_deploy_to_serverTests(unittest.TestCase):
  def setUp(self):
    self.manager = ServerManager()

  def test_remote_deploy_to_server_somedir(self):
    result = self.manager.remote_deploy_to_server('somedir')
    self.assertEqual(result, ServerDeployStatus.SUCCESS)

  def test_remote_deploy_to_server_otherdir(self):
    result = self.manager.remote_deploy_to_server('otherdir')
    self.assertEqual(result, ServerDeployStatus.FAILURE)


class doServerManager_server_statusTests(unittest.TestCase):
  def setUp(self):
    self.manager = ServerManager()

  def test_server_status_somedir(self):
    result = self.manager.server_status('somedir')
    self.assertEqual(result, ServerStatus.ONLINE)

  def test_server_status_otherdir(self):
    result = self.manager.server_status('otherdir')
    self.assertEqual(result, ServerStatus.OFFLINE)


class doServerManager_handle_serverTests(unittest.TestCase):
  def setUp(self):
    self.manager = ServerManager()

  def test_handle_server_somedir(self):
    result = self.manager.handle_server('somedir')
    self.assertEqual(result, ServerStatus.ONLINE)

  def test_handle_server_otherdir(self):
    result = self.manager.handle_server('otherdir')
    self.assertEqual(result, ServerStatus.OFFLINE)
