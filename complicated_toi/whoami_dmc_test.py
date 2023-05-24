from dmc import gettoken
from bearer import bearer
import http.client
import json
import logging

logging.basicConfig(level=logging.DEBUG)

headers = {
    "X-CENTRIFY-NATIVE-CLIENT": "true",
    "X-CFY-SRC": "python",
    "Authorization": "Bearer %s" % gettoken(var_dict['scope'])
}
conn = http.client.HTTPSConnection(var_dict['tenant_url'])
conn.request("POST", "/security/whoami", headers = headers)
response = conn.getresponse()
print(response.status)
ret = json.loads(response.read().decode())
print(ret["Result"]["User"])
