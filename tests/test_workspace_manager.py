#!/usr/bin/python

import unittest, os
from lib.workspace_manager import WorkspaceManager
from lib.model.models import Workspace
from lib.model.models import Project


class doWorkspaceManager_add_projectTests(unittest.TestCase):
  def setUp(self):
    self.manager = WorkspaceManager()

  def test_add_project(self):
    workspace = Workspace('somedir')
    project = Project('dir')
    result = self.manager.add_project(workspace, project)

    self.assertTrue(result.project_list)
    self.assertEqual(result.project_list[0].project_path, 'dir')


class doWorkspaceManager_find_vcs_projectsTests(unittest.TestCase):
  def setUp(self):
    self.manager = WorkspaceManager()

  def test_find_vcs_projects(self):
    # Join basedir of this project to /tests/test_data/workspace_manager
    path = os.path.join(os.getcwd())

    result = self.manager.find_vcs_projects(path)

    self.assertTrue(result.project_list)

    self.assertEqual(result.project_list[0].project_path, path)
