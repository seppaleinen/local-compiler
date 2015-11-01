#!/usr/bin/python

import unittest
import os
from lib.project_type_manager import ProjectTypeManager


class doProjectType_GuessLanguageTests(unittest.TestCase):
  def setUp(self):
    self.manager = ProjectTypeManager()

  def test_guess_language_python(self):
    python_folder = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data', 
      'python')

    result = self.manager.guess_language(python_folder)
    self.assertEqual(result.value, 'PYTHON')

  def test_guess_language_java(self):
    java_folder = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data', 
      'java')

    result = self.manager.guess_language(java_folder)
    self.assertEqual(result.value, 'JAVA')

  def test_guess_language_ruby(self):
    ruby_folder = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data', 
      'ruby')

    result = self.manager.guess_language(ruby_folder)
    self.assertEqual(result.value, 'RUBY')


class doProjectType_GuessBuildToolTests(unittest.TestCase):
  def setUp(self):
    self.manager = ProjectTypeManager()

  def test_guess_buildtool_maven(self):
    maven_folder = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data',
      'java',
      'maven')

    result = self.manager.guess_buildtool(maven_folder)

    self.assertEqual(result.value, 'MAVEN')

  def test_guess_buildtool_setup_tools(self):
    setup_tools_folder = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data',
      'python',
      'setuptools')

    result = self.manager.guess_buildtool(setup_tools_folder)

    self.assertEqual(result.value, 'SETUP_TOOLS')

  def test_guess_buildtool_bundler(self):
    bundler_folder = os.path.join(os.getcwd(), 
      'tests', 
      'test_data', 
      'project_type_manager_data',
      'ruby',
      'bundler')
    result = self.manager.guess_buildtool(bundler_folder)

    self.assertEqual(result.value, 'BUNDLER')
