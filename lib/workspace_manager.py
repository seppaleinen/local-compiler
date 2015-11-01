#!/usr/bin/python

from lib.model.models import Workspace, Project
import os


# Class responsible for managing workspaces
# Adding or removing projects from a workspace
class WorkspaceManager(object):
  def add_project(self, workspace, project):
    workspace.project_list.append(project)
    return workspace

  def find_vcs_projects(self, workspace_path):
    workspace = Workspace(workspace_path)

    for root, dirs, files in os.walk(workspace_path):
      for name in dirs:
        if name == '.git':
          git_dir = os.path.join(root, name)[:-5]
          workspace.project_list.append(Project(git_dir))

    return workspace
