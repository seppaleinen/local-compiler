#!/usr/bin/python

from model.enums import ServerDeployStatus
from model.enums import ServerStatus


# Class responsible for handling contact with server
class ServerManager(object):
  # Method for doing "Direct deploys", where you copy
  # the deploy-file to the server directly
  # Takes path to deploy-file and returns SERVER_DEPLOY_STATUS
  def direct_deploy_to_server(self, deployable_path):
    if deployable_path == 'somedir':
      return ServerDeployStatus.SUCCESS
    else:
      return ServerDeployStatus.FAILURE

  # Method for doing "Remote depoys", where you deploy
  # through ports.
  # Takes path to deploy-file and returns SERVER_DEPLOY_STATUS
  def remote_deploy_to_server(self, deployable_path):
    if deployable_path == 'somedir':
      return ServerDeployStatus.SUCCESS
    else:
      return ServerDeployStatus.FAILURE

  # Method for seeing if server is online or offline
  # Takes server-name as parameter and returns result
  def server_status(self, server_name):
    if server_name == 'somedir':
      return ServerStatus.ONLINE
    else:
      return ServerStatus.OFFLINE

  # Method for starting, stopping or restarting server
  # Takes name of server as parameter and returns result
  def handle_server(self, server_name):
    if server_name == 'somedir':
      return ServerStatus.ONLINE
    else:
      return ServerStatus.OFFLINE
