#Basic example on how to use API
#get token from tenant UI
import requests
import json
#Get the UI from the tenant
token = None
#example abc0123.my.centrify.net
tenant_url = None
headers =  {
"X-CENTRIFY-NATIVE-CLIENT": "true",
"Content-Type" : "application/json",
"Authorization": "Bearer %s" % token
} 
# Input vars for the user
name = None
email = None
password = None
#Add Cdir user
auri = "https://{0}/CDirectoryService/CreateUser".format(tenant_url)
abody = {'Name': name, 'Password': password, 'Mail': email}
areq = requests.post(url=auri, headers=headers, json=abody).json()
print('Add URL is {0}'.format(auri))
print("Add JSON is:  {}".format(json.dumps(areq)))
#query ID of Cdir user
quri = "https://{0}/Redrock/query".format(tenant_url)
qbod = {'Script': "Select ID from User WHERE Username = '{0}'".format(name)}
ql = requests.post(url=quri, headers=headers, json=qbod).json()
qlj = json.dumps(ql)
qljl = (json.loads(qlj))
print("Query JSON is:  {0}".format(qlj))
#Delete Cdir User
duri = "https://{0}/CDirectoryService/DeleteUser".format(tenant_url) 
dbody = {'ID': '{0}'.format(qljl["Result"]["Results"][0]["Row"]['ID'])}
print('Url is: {0}'.format(duri)) 
print('Body is {0}'.format(dbody))
dr = requests.post(url=duri, headers=headers, json=dbody).json()
print(json.dumps(dr))