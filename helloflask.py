from flask import Flask
import os.path
from ConfigParser import SafeConfigParser

app = Flask(__name__)

# get configuration
config = SafeConfigParser()
thisdir = os.path.dirname(__file__)
parentdir = '/'.join(thisdir.split('/')[:-1])
config.readfp(open(os.path.join(parentdir, 'helloflask.cfg')))
appconfig = dict(config.items('app'))

@app.route("/")
def hello():
    return "Hello World!\n{}".format(appconfig)

if __name__ == "__main__":
    app.run()