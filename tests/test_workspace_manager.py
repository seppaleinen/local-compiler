#!/usr/bin/python

import unittest
from lib.workspace_manager import WorkspaceManager
from lib.model.models import Workspace, Project


class doWorkspaceManagerTests(unittest.TestCase):
  def setUp(self):
    self.manager = WorkspaceManager()

  def test_add_project(self):
    workspace = Workspace()
    project = Project('dir')
    result = self.manager.add_project(workspace, project)

    self.assertTrue(result.project_list)
    self.assertEqual(result.project_list[0].project_path, 'dir')

  def test_find_vcs_projects(self):
    result = self.manager.find_vcs_projects('somedir')

    self.assertFalse(result.project_list)
