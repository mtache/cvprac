# Copyright (c) 2020 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

from cvprac.cvp_client import CvpClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Create connection to CloudVision
clnt = CvpClient()
clnt.connect(['10.83.13.33'],'cvpadmin', 'arastra')

# Get parent container information
parent = clnt.api.get_container_by_name("ContainerA")

# Create new container ContainerB under ContainerA

clnt.api.add_container("ContainerB",parent["name"],parent["key"])