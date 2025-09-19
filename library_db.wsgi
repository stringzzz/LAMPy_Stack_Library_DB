# library_db.wsgi
import sys
sys.path.insert(0, '/var/www/html') # Adjust path if needed

from library_db import app as application # Assuming 'app' is your Flask/Django application instance