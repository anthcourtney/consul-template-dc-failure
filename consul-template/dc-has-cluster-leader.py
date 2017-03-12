#!/usr/bin/env python
import os
import sys
import requests

if len(sys.argv) > 1 and "CONSUL_ADDR" in os.environ:
  dc = sys.argv[1]
  # query consul
  r = requests.get( "http://" + os.environ['CONSUL_ADDR'] + "/v1/catalog/services", params={ 'dc': dc }, timeout=5)
  if r.status_code == requests.codes.ok:
    print "true"
  else:
    print "false"
elif len(sys.argv) > 1:
  # dc provided, but no consul_addr set, so we can't verify. Therefore assume cluster leader exists
  print "true"
else:
  # No argv = no dc = no cluster leader
  print "false"
