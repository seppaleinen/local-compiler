#!/usr/bin/python

from model.compile_info import LANGUAGE


class CompilingManager(object):
  def guess_project_language_and_builder(self, project_dir):
    return LANGUAGE.JAVA
