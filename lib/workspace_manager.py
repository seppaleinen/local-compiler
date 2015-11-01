#!/usr/bin/python

from lib.model.models import Workspace, Project
import os


class WorkspaceManager(object):
  def add_project(self, workspace, project):
    workspace.project_list.append(project)
    return workspace

  def find_vcs_projects(self, workspace_path):
    workspace = Workspace(workspace_path)

    for root, dirs, files in os.walk(workspace_path):
      print(dirs)
      for name in dirs:
        if name == '.git':
          print(name)
          git_dir = os.path.join(root, name)[:-5]
          print(git_dir)
          workspace.project_list.append(Project(git_dir))

    return workspace
