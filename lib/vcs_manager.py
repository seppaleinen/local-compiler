#!/usr/bin/python

import subprocess
import os

def git_command(vcs_path, command):
  git_dir=os.path.join(vcs_path, '.git')

  git_command = ['git', '--work-tree=' + vcs_path, '--git-dir=' + git_dir, command]

  return subprocess.Popen(git_command, stdout=subprocess.PIPE).communicate()[0]


# Class responsible for handling contact with vcs repositories
class VcsManager(object):
  # Method for checking version control status
  # Takes path of version control and returns result
  def status(self, vcs_path):
    return git_command(vcs_path, 'status')

  # Method for updating version control repository
  # Takes path of directory and returns result
  def update(self, vcs_path):
    return git_command(vcs_path, 'pull')
