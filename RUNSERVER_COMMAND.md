To successfully preview and run the JWQL Django application, ensure the following:

1. The server is started with:
   ```
   python manage.py runserver 0.0.0.0:3001
   ```
   (This binds to 0.0.0.0 on port 3001, required for containerized/remote preview.)

2. The configuration file `jwql/config.json` **must exist** at runtime in the expected directory.
   - Example required file: `spacetelescope/jwql/config.json` (or its correct location if otherwise documented).
   - If this file is missing or incorrect, critical runtime errors will occur and the preview system will fail to start.
   - See the example config or documentation for required contents and structure.

3. All essential Python runtime dependencies **must** be listed in `requirements.txt`. (This now explicitly includes `inflection` and other direct imports.)
