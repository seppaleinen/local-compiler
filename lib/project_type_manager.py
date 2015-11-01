#!/usr/bin/python

from model.enums import Language
from model.enums import BuildTool
import os


# Class responsible for guessing which language and build-tool is
# to be used on a certain directory path
class ProjectTypeManager(object):
  def guess_language(self, project_dir):
    guestimate = None

    for item in os.listdir(project_dir):
      file_path = os.path.join(project_dir, item)
      if os.path.isfile(file_path):
        if('.py' in file_path):
          guestimate = Language.PYTHON
        elif('.java' in file_path):
          guestimate = Language.JAVA
        elif('.rb' in file_path):
          guestimate = Language.RUBY
        else:
          guestimate = Language.UNKNOWN

    return guestimate

  def guess_buildtool(self, project_dir):
    guestimate = None

    for item in os.listdir(project_dir):
      file_path = os.path.join(project_dir, item)
      if os.path.isfile(file_path):
        if('setup.py' in file_path):
          guestimate = BuildTool.SETUP_TOOLS
        elif('pom.xml' in file_path):
          guestimate = BuildTool.MAVEN
        elif('.gemspec' in file_path):
          guestimate = BuildTool.BUNDLER
        else:
          guestimate = Language.UNKNOWN

    return guestimate
