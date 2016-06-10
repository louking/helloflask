USERNAME = 'scoretility'
SERVER = 'hello.scoretility.org'
APP_NAME = 'helloflask'
PROJECT_DIR = '/var/www/%s/%s' % (SERVER, APP_NAME)
WSGI_SCRIPT = 'application.wsgi'

env.hosts = ["%s@%s" % (USERNAME, SERVER)]

def deploy():
    with cd(PROJECT_DIR):
        run('git pull')
        run('bin source/activate')
        run('pip install -r requirements.txt')
        run('touch %s' % WSGI_SCRIPT)