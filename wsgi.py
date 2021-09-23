import sys
import site

# site.addsitedir('/home/aresqubitadmin/env/lib/python3.6/site-packages')

# sys.path.insert(0, '/var/www/creditIA')

activate_this = '/home/aresqubitadmin/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# site.addsitedir('/home/aresqubitadmin/env/lib/python3.6/site-packages')

sys.path.insert(0, '/var/www/creditIA')
from app import app as application


