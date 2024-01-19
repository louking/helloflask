from fabric.api import env, run, cd

USERNAME = 'scoretility'
SERVER = 'hello.scoretility.com'
APP_NAME = 'helloflask'
PROJECT_DIR = '/var/www/%s/%s' % (SERVER, APP_NAME)
WSGI_SCRIPT = 'application.wsgi'

env.hosts = ["%s@%s" % (USERNAME, SERVER)]

def deploy(branch='master'):
    with cd(PROJECT_DIR):
        run('git pull')
        run('git checkout {}'.format(branch))
        run('source bin/activate; pip install -r requirements.txt')
        run('touch %s' % WSGI_SCRIPT)