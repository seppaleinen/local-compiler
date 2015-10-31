#!/usr/bin/python


class Project(object):
  def __init__(self, project_path=''):
    self.project_path = project_path


class Workspace(object):
  def __init__(self, project_list = []):
    self.project_list = project_list
