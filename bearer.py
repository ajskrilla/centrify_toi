import requests
import json
import logging
import getpass
#give example site of python
#logging for the shell. Note, u can make a logging util file to do all of this
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
    )
try:
    from dmc import gettoken
except ImportError:
    logging.error("DMC is not installed, please use OAUTH only.")
var_dict = {
    'auth_type' : None,
    #example of url: abc0123.my.centfrify.net
    'tenant_url' : None,
    'scope' : None,
    # can implement this in the dict and have it not prompt
    'password' : None,
    'svc_account' : None,
    'appid' : None
    }
if var_dict.get('auth_type').upper() == 'DMC':
#DMC is harvey's lib:
#https://github.com/centrify/dmc-python
    try:
        logging.info('Token Recieved')
        logging.info('Token val is :          %s' % gettoken(var_dict['scope']))
    except:
        logging.error("fatal error. check error thrown from dmc lib.")
elif var_dict.get('auth_type').upper() == 'OAUTH':
    #can remove the prompt. Just need to uncomment the dict and then set the variable 
    password = getpass.getpass('Please provide the password for account {0}'.format(var_dict['svc_account']))
    #to see if any of the req variables are null
    if var_dict['appid'] == None or var_dict['svc_account'] == None or password == None:
        logging.error('Need to input required variable')
    else:
        headers = {
        'X-CENTRIFY-NATIVE-CLIENT': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
            }
        body = {
        'client_id': var_dict['svc_account'],
        'client_secret': password,
        'scope': var_dict['scope'],
        'grant_type': 'client_credentials'
            }
        url = "https://{0}/Oauth2/Token/{1}".format(var_dict['tenant_url'], var_dict['appid'])
        logging.info('URL of token is: %s' % url)
        try:
            #in Requests lib, u need to do data as an argument cuz of the Content type
            req = requests.post(url=url, headers=headers,data=body).json()
            logging.info("Token Is:       %s" % req['access_token'])
            token = req['access_token']
        except:
            logging.error('Issue getting token')
            logging.error('JSON dump of request: %s' % json.dumps(req))
else:
    logging.error('Please use a correct auth type')
#grab the token output and go to API.py to set as variable manually