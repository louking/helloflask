from . import app
from flask.views import MethodView

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
