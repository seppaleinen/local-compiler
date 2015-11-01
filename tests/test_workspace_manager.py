#!/usr/bin/python

import unittest, os
from lib.workspace_manager import WorkspaceManager
from lib.model.models import Workspace, Project


class doWorkspaceManagerTests(unittest.TestCase):
  def setUp(self):
    self.manager = WorkspaceManager()

  def test_add_project(self):
    workspace = Workspace('somedir')
    project = Project('dir')
    result = self.manager.add_project(workspace, project)

    self.assertTrue(result.project_list)
    self.assertEqual(result.project_list[0].project_path, 'dir')

  def test_find_vcs_projects(self):
    # Join basedir of this project to /tests/test_data/workspace_manager
    path = os.path.join(os.getcwd(), 'tests', 'test_data', 'workspace_manager')
    
    result = self.manager.find_vcs_projects(path)

    self.assertTrue(result.project_list)

    expected_path_1 = os.path.join(path, 'project1')
    expected_path_2 = os.path.join(path, 'project2')

    self.assertEqual(result.project_list[0].project_path, expected_path_1)
    self.assertEqual(result.project_list[1].project_path, expected_path_2)
