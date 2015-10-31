#!/usr/bin/python

from model.enums import Language
from model.enums import BuildTool


# Class responsible for guessing which language and build-tool is
# to be used on a certain directory path
class ProjectTypeManager(object):
  def guess_language(self, project_dir):
    return Language.JAVA

  def guess_buildtool(self, project_dir):
    return BuildTool.MAVEN
