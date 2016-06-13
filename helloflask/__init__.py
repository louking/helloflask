from ConfigParser import SafeConfigParser
import os.path
import pprint
pp = pprint.PrettyPrinter(indent=4)

from app import app

print 'init fired'

# get configuration
config = SafeConfigParser()
thisdir = os.path.dirname(__file__)
sep = os.path.sep
parentdir = sep.join(thisdir.split(sep)[:-1])
config.readfp(open(os.path.join(parentdir, 'helloflask.cfg')))
appconfig = config.items('app')

# apply configuration to app
# eval is safe because this configuration is controlled at root
for key,value in appconfig:
    try:
        app.config[key.upper()] = eval(value)
    except SyntaxError:
        app.config[key.upper()] = value

pp.pprint(app.config)

import views