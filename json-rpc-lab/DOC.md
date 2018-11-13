UPDATED: 11/12/18

## jrpcserver.py jrpcclient.py node.py

* TO RUN: ./jrpcserver.py    THEN   ./jrpcclient.py

## PRINCIPLE OF OPERATION:
jrpcclient.py:

* initialize tree and connection to server
* call show() to print out the tree
* tree is initially made of nodes, it needs to be converted to a dictionary using treetodict() found in node.py
* server.increment() is called to increment all values in the in the dictionary
* tonode() is used to convert back to a node based tree
* show() is called to print out the updated tree

jrpcserver.py:

* connection is initialized to listen for requests
* increment() is called to perform requests
* a dump of the incoming request to sent to request.json
* inc() is used to perform the acutal incrementation of that values in the dictionary
* updated dict is returned to client
