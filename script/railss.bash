#!/bin/bash

# ~/tsds/script/railss.bash

# This script should start rails server on all IPs so I can see the app from another host.

cd ~/tsds/
bin/rails s -b 0.0.0.0 -p 3010
# 0.0.0.0 declares that I want rails listening on all IPs bound to this host.
exit

