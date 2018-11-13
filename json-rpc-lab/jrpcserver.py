#! /usr/bin/env python

# minimalistic server example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
from node import *
import json

# Helper for increment func
def inc(g):
  g['val'] += 1
  for c in g['children']:
	  inc(c)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def increment(self, g):
	# create json dump, increment
	with open('request.json', 'w') as f:
         json.dump(g, f)
	inc(g)
	return g


# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)
print("Server initiated")

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
