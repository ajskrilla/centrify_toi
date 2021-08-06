# centrify_toi
Centrify TOI ExamplesTOI
PAS API TOI:
Technically, you can use any major language to make REST calls, but this is a basic overview of how to use in VSCode/ Setup Python3.
Setup:
	a. Where to download VSCode:
		https://code.visualstudio.com/
		#extension for vscode. Need to restart after install
		https://marketplace.visualstudio.com/items?itemName=ms-python.python
	b. Set up the code and open up a file and rename to bearer.py
	c. Go over the necessary set up for Python3
		https://www.python.org/downloads/release/python-386/
		BE SURE TO HAVE IT DO CUSTOM DOWNLOAD AND SELECT IT TO ADD ENV VARIABLES
	d. install the libraries:
		1. requests
		2. centriy.dmc
		3. pywin32 (Win Env)
Execution:
	Leverage the simple toi script
		a. Named sample_toi.py
		b. Input the token from the UI of the oauth client
		c. Discuss the packet structure of the headers and body of each call
		d. Go over each API endpoint
	#NOTE the logging portion is to cleanly print in UI
	a. Example file (bearer.py) to be used to get bearer token for the next steps:
		1. Header packet
		2. Request requests
		3. Print/Log token
		Auth Types:
			OAUTH
			DMC
	b. Example File (API.py) to do these actions and log:
		1. Add account
		2. Query ID of account 
		3. Delete Account
	c. Both files interact with one another
Example files will be attached. One set will be basic, the other set will be a more complicated example
