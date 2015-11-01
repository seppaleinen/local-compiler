#!/usr/bin/python

import unittest
import os
import mock
from lib.compiling_manager import CompilingManager
from lib.model.enums import BuildTool


class doCompilerTests(unittest.TestCase):
  def setUp(self):
    self.manager = CompilingManager()

  @mock.patch('lib.compiling_manager.subprocess')
  def test_compile_project_custom_script(self, mocked):
    setup_path = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data', 
      'python', 
      'setuptools')
    setup_py = os.path.join(setup_path, 'setup.py')

    result = self.manager.compile_project(
      setup_path, 
      BuildTool.UNKNOWN, 
      custom_build_script=['python', setup_py, 'install'])
    mocked.Popen.assert_called_with(['python', setup_py, 'install'], stdout=mocked.PIPE)

  @mock.patch('lib.compiling_manager.subprocess')
  def test_compile_project_setup_tools(self, mocked):
    setup_path = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data', 
      'python', 
      'setuptools')

    result = self.manager.compile_project(
      setup_path, 
      BuildTool.SETUP_TOOLS)
    mocked.Popen.assert_called_with(['python', os.path.join(setup_path, 'setup.py'), 'install'], stdout=mocked.PIPE)

  @mock.patch('lib.compiling_manager.subprocess')
  def test_compile_project_maven(self, mocked):
    maven_path = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data', 
      'java', 
      'maven')

    result = self.manager.compile_project(
      maven_path, 
      BuildTool.MAVEN)

    mocked.Popen.assert_called_with(['mvn', 'clean', 'install', '-f', os.path.join(maven_path, 'pom.xml')], stdout=mocked.PIPE)

