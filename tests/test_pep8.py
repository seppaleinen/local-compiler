#!/usr/bin/python

import unittest
import pep8
import os
import os.path

ignore_patterns = ('.svn', 'bin', 'lib' + os.sep + 'python')

def ignore(dir):
  """Should the directory be ignored?"""
  for pattern in ignore_patterns:
    if pattern in dir:
      return True
  return False


class doPep8Tests(unittest.TestCase):
    def setUp(self):
        self.pep8style = pep8.StyleGuide(quiet=False)

    def test_pep8e(self):
        errors = 0
        path = os.path.join(os.getcwd(), 'lib')
        for root, _, files in os.walk(path):
            if ignore(root):
                continue

        python_files = [os.path.join(root, f) for f in files if f.endswith('.py')]

        errors += self.pep8style.check_files(python_files).total_errors

        self.assertEqual(errors, 0, 'PEP8 style errors: %d' % errors)
