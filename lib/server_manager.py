#!/usr/bin/python

# Class responsible for handling contact with server
class ServerManager(object):
  # Method for doing "Direct deploys", where you copy
  # the deploy-file to the server directly
  # Takes path to deploy-file and returns result
  def direct_deploy_to_server(self, deployable_path):
    return 'result'

  # Method for doing "Remote depoys", where you deploy
  # through ports.
  # Takes path to deploy-file and returns result 
  def remote_deploy_to_server(self, deployable_path):
    return 'result'

  # Method for seeing if server is online or offline
  # Takes server-name as parameter and returns result
  def server_status(self, server):
    return 'result'

  # Method for starting, stopping or restarting server
  # Takes name of server as parameter and returns result
  def handle_server(self, server_name):
    return 'result'