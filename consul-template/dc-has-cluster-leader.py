#!/usr/bin/env python
import os
import sys
import requests

consul_var = "CONSUL_ADDR"
result = "false"

if len(sys.argv) > 1 and consul_var in os.environ:
  dc = sys.argv[1]
  # query consul
  r = requests.get( "http://" + os.environ[consul_var] + "/v1/catalog/services", params={ 'dc': dc })
  if r.status_code == requests.codes.ok:
    result = "true"
elif len(sys.argv) > 1:
  # dc provided, but no consul_addr set, so we can't verify. Therefore assume cluster leader exists
  result = "true"

# Exit
print result
sys.exit(0)
