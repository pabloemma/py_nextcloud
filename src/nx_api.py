import sys
import os
from os.path import dirname
from os.path import join

sys.path.insert(0, join(dirname(__file__), 'src'))

from nextcloud import NextCloud



#NEXTCLOUD_URL = "http://{}:80".format(os.environ['NEXTCLOUD_HOSTNAME'])
NEXTCLOUD_URL = "http://casitadongaspar.com/nextcloud"
NEXTCLOUD_USERNAME = "pabloemma"
NEXTCLOUD_PASSWORD = "?Pa!blo?nuke"

# True if you want to get response as JSON
# False if you want to get response as XML
to_js = True

nxc = NextCloud(endpoint=NEXTCLOUD_URL, user=NEXTCLOUD_USERNAME, password=NEXTCLOUD_PASSWORD, json_output=to_js)
users = nxc.get_users()

print(users)
curl -X GET --user "pabloemma" https://casitadongaspar.com/nextcloud/remote.php/dav/files/pabloemma/Nextcloud.png --output nextcloud.png
curl --user "pabloemma" -T /Users/klein/iperf.log https://casitadongaspar.com/nextcloud/remote.php/dav/files/pabloemma/Temperature/