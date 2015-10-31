#!/usr/bin/python

from lib.model.models import Workspace


class WorkspaceManager(object):
  def add_project(self, workspace, project):
    workspace.project_list.append(project)
    return workspace

  def find_vcs_projects(self, workspace_path):
    workspace = Workspace(workspace_path)
    return workspace
