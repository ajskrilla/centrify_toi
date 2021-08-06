import logging
import requests
import json
#change back to bearer
from bearer import bearer
import traceback

# construct class
b =  bearer()
token = b.token_return()
var_dict = b.dict_ret()
#logging for the shell. Note, u can make a logging util file to do all of this
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
    )
#set the variables here for new cdir user
name = None
email = None
password = None
try:
    #will error out if the key value is not there OR the dict is not there 
    auth_type = var_dict['auth_type']
    tenant_url = var_dict['tenant_url']
    if auth_type == None or tenant_url == None:
        logging.error('Please set the values in other file. This will not work without that')
except (AttributeError, KeyError):
    logging.error('Failed to import the dict values. Were they set in bearer.py or is the file not in the dir?')
#set the headers from the token value
if auth_type.upper() == 'DMC':
    headers =  {
    #example of dmc header
    "X-CENTRIFY-NATIVE-CLIENT": "true",
    "X-CFY-SRC": "python",
    "Authorization": "Bearer %s" % token
    }
    logging.info('dmc headers set successfully')
elif auth_type.upper() == 'OAUTH':    
    #example of oauth header
    headers =  {
    "X-CENTRIFY-NATIVE-CLIENT": "true",
    "Content-Type" : "application/json",
    "Authorization": "Bearer %s" % token
    }    
    logging.info('oauth headers set successfully')
else:
    logging.error('Not a valid auth type.')
#exmples of API calls to use. Can structure this however
#https://developer.centrify.com/docs/create-and-manage-cloud-directory-users-_new
def add_query_delete(name = name, password = password, email = email):
    if name == None or password == None:
        logging.error('Set the name and password vars')
    #add cdir user uri
    auri = "https://{0}/CDirectoryService/CreateUser".format(tenant_url)
    abody = {'Name': name, 'Password': password, 'Mail': email}
    logging.info('Url is: {0}'.format(auri)) 
    logging.info('Body is {0}'.format(abody))
    logging.info("Adding Account....")
    try:
        br = requests.post(url=auri, headers=headers, json=abody).json()
        brj = json.dumps(br)
        lbrj = json.loads(brj)
        logging.info("JSON dump of adding account is: {0}".format(brj))
        if lbrj["success"] == False:
            logging.error("Error Occurred adding account.")
        else:
            logging.info('Account Added.')
    except:
        logging.error('Issue adding account. JSON dump is: {0}'.format(json.dumps(br)))
    #query c dir account  uri
    quri = "https://{0}/Redrock/query".format(tenant_url)
    qbod = {'Script': "Select ID from User WHERE Username = '{0}'".format(name)}
    logging.info('URL is {0}'.format(quri))
    logging.info('Querying account.......')
    try:
        ql = requests.post(url=quri, headers=headers, json=qbod).json()
        qlj = json.dumps(ql)
        qljl = (json.loads(qlj))
        if qljl["success"] == False:
            logging.error("Error Occurred")
        else:
            logging.info('JSON dump of querying account is: {0}'.format(qlj)) 
            logging.info("Found Account.")
    except:
        logging.error("Issue adding accout, JSON dump: {0}".format(qlj))
    #delete c dir account uri
    duri = "https://{0}/CDirectoryService/DeleteUser".format(tenant_url) 
    dbody = {'ID': '{0}'.format(qljl["Result"]["Results"][0]["Row"]['ID'])}
    logging.info('Url is: {0}'.format(duri)) 
    logging.info('Body is {0}'.format(dbody))
    logging.info("Deleting Account....")
    try: 
        dr = requests.post(url=duri, headers=headers, json=dbody).json()
        drj = json.dumps(dr)
        ldrj = json.loads(drj)
        if ldrj["success"] == False:
            logging.error("Error Occurred")
        else:
            logging.info("JSON dump of deleting account is: {0}".format(json.dumps(dr)))
            logging.info('Account Deleted.')
    except:
        logging.error('Issue deleting account.')
try:
    add_query_delete()
except:
    logging.error("Internal error occurred")
    print(traceback.print_exc())