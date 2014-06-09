web: gunicorn --pythonpath="$PWD/cdzforever" wsgi:application
worker: python manage.py rqworker high default low
