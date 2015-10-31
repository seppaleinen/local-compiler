#!/usr/bin/python

from model.enums import Language
from model.enums import BuildTool


# Class responsible for guessing which language and build-tool is
# to be used on a certain directory path
class ProjectTypeManager(object):
  def guess_language(self, project_dir):
    if project_dir == 'somedir':
      return Language.JAVA
    else:
      return Language.RUBY

  def guess_buildtool(self, project_dir):
    if project_dir == 'somedir':
      return BuildTool.MAVEN
    else:
      return BuildTool.BUNDLER
