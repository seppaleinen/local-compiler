#!/usr/bin/python

from model.enums import BuildTool
import subprocess
import os


def process(script):
  result = None

  if script is not None:
    result = subprocess.Popen(script, stdout=subprocess.PIPE).communicate()[0]

  return result


class CompilingManager(object):
  def compile_project(self, project_dir, build_tool, custom_build_script=None):
    if(build_tool == BuildTool.SETUP_TOOLS):
      custom_build_script = ['python', os.path.join(project_dir, 'setup.py'), 'install']
    elif(build_tool == BuildTool.MAVEN):
      custom_build_script = ['mvn', 'clean', 'install', '-f', os.path.join(project_dir, 'pom.xml')]

    return process(custom_build_script)
