# Send a GET request to a given URL with a header variable.

#!/bin/bash

url=$1

curl -s -H "X-HolbertonSchool-User-Id: 98" "$url"
