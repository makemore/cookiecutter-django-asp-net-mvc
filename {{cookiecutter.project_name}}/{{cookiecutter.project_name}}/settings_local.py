

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{cookiecutter.project_name}}',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '', #below lines commented to connect via sockets, without a password. TCP connection requires password
        #'PASSWORD': '',
        #'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        #'PORT': '',                      # Set to empty string for default.
    }
}
"""

USE_X_FORWARDED_HOST = False

COMPRESS_ENABLED = True