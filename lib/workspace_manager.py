#!/usr/bin/python

from lib.model.models import Workspace, Project


class WorkspaceManager(object):
  def add_project(self, workspace, project):
    workspace.project_list.append(project)
    return workspace

  def find_vcs_projects(self, workspace_path):
    workspace2 = Workspace()
    return workspace2
