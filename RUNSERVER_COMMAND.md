To launch the Django server for local development, use:

python manage.py runserver 0.0.0.0:3001

This binds the web server to all interfaces (useful for containerization) and sets the port to 3001, as required for this container.

Note: Make sure you've installed all requirements via
pip install -r requirements.txt

If you wish to specify a settings module:
python manage.py runserver 0.0.0.0:3001 --settings=jwql.settings
