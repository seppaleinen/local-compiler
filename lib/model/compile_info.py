#!/usr/bin/python

from enum import Enum


class LANGUAGE(Enum):
  JAVA = 'JAVA'
  PYTHON = 'PYTHON'
  RUBY = 'RUBY'
  UNKNOWN = 'UNKNOWN'

class BUILD_TOOL(Enum):
	MAVEN = 'MAVEN'
	SETUP_TOOLS = 'SETUP_TOOLS'
	BUNDLER = 'BUNDLER'
	UNKNOWN = 'UNKNOWN'
