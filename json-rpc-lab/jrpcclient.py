#! /usr/bin/env python

# minimalistic client example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
from node import *

def tonode(g):
	child = []

	for i, c in enumerate(g['children']):
		child.append(node(c['name'], c['children']))
		child[i].val = c['val']

	n = node("root", child)
	n.val = g['val']
	return n

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

# initialize tree
leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()

# do this increment remotely:
rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

# Convert to dict to transfer
root = root.treetodict()

# Execute in server:
root = server.increment(root)

# Convert dict back to tree
root = tonode(root)

print("graph after increment")
root.show()

rpc.close() # Closes the socket 's' also
