import os, sys
from ConfigParser import SafeConfigParser

# get configuration
config = SafeConfigParser()
config.read('./helloflask.cfg')
PROJECT_DIR = config.get('project', 'PROJECT_DIR')

# activate virtualenv
activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from helloflask import app as application