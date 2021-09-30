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

class bearer:
    def __init__(self):
        self.var_dict = {
            'auth_type' : None,
            #example of url: abc0123.my.centfrify.net
            'tenant_url' : None,
            'scope' : None,
            # OAUTH section. Enter all needed
            # can implement this in the dict and have it not prompt
            #'password' : "",
            #'svc_account' : "",
            #'appid' : ""
            }
        if self.var_dict.get('auth_type').upper() == 'DMC':
        #DMC is harvey's lib:
        #https://github.com/centrify/dmc-python
            try:
                self.token = gettoken(self.var_dict['scope'])
                logging.info('Token Recieved')
                logging.info('Token val is :          %s' % self.token)
            except:
                logging.error("fatal error. check error thrown from dmc lib.")
        elif self.var_dict.get('auth_type').upper() == 'OAUTH':
            if not self.var_dict['password']:
                #can remove the prompt. Just need to uncomment the dict and then set the variable 
                password = getpass.getpass('Please provide the password for account {0}'.format(self.var_dict['svc_account']))
            else:
                password = self.var_dict['password']
            #to see if any of the req variables are null
            if self.var_dict['appid'] == None or self.var_dict['svc_account'] == None or self.var_dict['password'] == None:
                logging.error('Need to input required variable')
            else:
                headers = {
                'X-CENTRIFY-NATIVE-CLIENT': 'true',
                'Content-Type': 'application/x-www-form-urlencoded'
                    }
                body = {
                'client_id': self.var_dict['svc_account'],
                'client_secret': password,
                'scope': self.var_dict['scope'],
                'grant_type': 'client_credentials'
                    }
                url = "https://{0}/Oauth2/Token/{1}".format(self.var_dict['tenant_url'], self.var_dict['appid'])
                logging.info('URL of token is: %s' % url)
                try:
                    #in Requests lib, u need to do data as an argument cuz of the Content type
                    req = requests.post(url=url, headers=headers,data=body).json()
                    logging.info("Token Is:       %s" % req['access_token'])
                    self.token = req['access_token']
                except:
                    logging.error('Issue getting token')
                    logging.error('JSON dump of request: %s' % json.dumps(req))
        else:
            logging.error('Please use a correct auth type')
    def dict_ret(self):
        return self.var_dict
    def token_return(self):
        return self.token

