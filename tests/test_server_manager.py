#!/usr/bin/python

import unittest
from lib.server_manager import ServerManager
from lib.model.enums import ServerDeployStatus, ServerStatus


class doServerManagerTests(unittest.TestCase):
  def setUp(self):
    self.manager = ServerManager()

  def test_direct_deploy_to_server(self):
    result = self.manager.direct_deploy_to_server('somedir')
    self.assertEqual(result, ServerDeployStatus.SUCCESS)

  def test_remote_deploy_to_server(self):
    result = self.manager.remote_deploy_to_server('somedir')
    self.assertEqual(result, ServerDeployStatus.SUCCESS)

  def test_server_status(self):
    result = self.manager.server_status('somedir')
    self.assertEqual(result, ServerStatus.ONLINE)

  def test_handle_server(self):
    result = self.manager.handle_server('somedir')
    self.assertEqual(result, ServerStatus.ONLINE)
