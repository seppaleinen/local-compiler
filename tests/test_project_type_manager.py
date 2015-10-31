#!/usr/bin/python

import unittest
from lib.project_type_manager import ProjectTypeManager


class doProjectType_GuessLanguageTests(unittest.TestCase):
  def setUp(self):
    self.manager = ProjectTypeManager()

  def test_guess_language_somedir(self):
    result = self.manager.guess_language('somedir')
    self.assertEqual(result.value, 'JAVA')

  def test_guess_language_otherdir(self):
    result = self.manager.guess_language('otherdir')
    self.assertEqual(result.value, 'RUBY')


class doProjectType_GuessBuildToolTests(unittest.TestCase):
  def setUp(self):
    self.manager = ProjectTypeManager()

  def test_guess_buildtool_somedir(self):
    result = self.manager.guess_buildtool('somedir')
    self.assertEqual(result.value, 'MAVEN')

  def test_guess_buildtool_otherdir(self):
    result = self.manager.guess_buildtool('otherdir')
    self.assertEqual(result.value, 'BUNDLER')
