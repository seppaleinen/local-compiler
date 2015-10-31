#!/usr/bin/python

import unittest
from lib.workspace_manager import WorkspaceManager
from lib.model.models import Workspace, Project


class doWorkspaceManagerTests(unittest.TestCase):
  def setUp(self):
    self.manager = WorkspaceManager()

  def test_find_vcs_projects(self):
    result = self.manager.find_vcs_projects('somedir')

    self.assertFalse(result.project_list)
