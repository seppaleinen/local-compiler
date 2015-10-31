#!/usr/bin/python

from model.compile_info import LANGUAGE
from model.compile_info import BUILD_TOOL

# Class responsible for guessing which language and build-tool is
# to be used on a certain directory path
class ProjectTypeManager(object):
  def guess_language(self, project_dir):
    return LANGUAGE.JAVA

  def guess_buildtool(self, project_dir):
    return BUILD_TOOL.MAVEN