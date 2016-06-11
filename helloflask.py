from flask import Flask
import os.path
from ConfigParser import SafeConfigParser
from flask.views import MethodView

app = Flask(__name__)

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

@app.route("/")
def hello():
    return "Hello World!"

#######################################################################
class ViewDebug(MethodView):
#######################################################################
    
    #----------------------------------------------------------------------
    def get(self):
    #----------------------------------------------------------------------
        try:
            # collect app.config variables
            configkeys = app.config.keys()
            configkeys.sort()
            appconfig = []
            for key in configkeys:
                value = app.config[key]
                appconfig.append({'label':key, 'value':value})

            thistable = '<table>\n<thead><tr><th>Name</th><th>Value</th></tr></thead>\n<tbody>\n'

            for item in appconfig:
                thistable += '<tr><td>{}</td><td>{}</td></tr>\n'.format(item['label'], item['value'])

            thistable += '</tbody>\n</table>'
            return thistable

        except:
            raise
#----------------------------------------------------------------------
app.add_url_rule('/debug',view_func=ViewDebug.as_view('debug'),methods=['GET'])
#----------------------------------------------------------------------

if __name__ == "__main__":
    app.run()