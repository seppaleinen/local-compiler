#!/usr/bin/python

from enum import Enum


class Language(Enum):
  JAVA = 'JAVA'
  PYTHON = 'PYTHON'
  RUBY = 'RUBY'
  UNKNOWN = 'UNKNOWN'


class BuildTool(Enum):
  MAVEN = 'MAVEN'
  SETUP_TOOLS = 'SETUP_TOOLS'
  BUNDLER = 'BUNDLER'
  UNKNOWN = 'UNKNOWN'


class ServerDeployStatus(Enum):
  SUCCESS = 'SUCCESS'
  FAILURE = 'FAILURE'


class ServerStatus(Enum):
  ONLINE = 'ONLINE'
  OFFLINE = 'OFFLINE'
