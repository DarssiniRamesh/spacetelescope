# Django Static Files Configuration

## Overview
This document explains the static files configuration for the JWQL Django application.

## Configuration Details

### Static Files Settings (settings.py)

1. **STATIC_URL**: Set to `/static/` - this is the URL prefix for serving static files
2. **STATICFILES_DIRS**: Conditionally includes project-level static directory only if it contains files
3. **STATICFILES_FINDERS**: Uses both FileSystemFinder and AppDirectoriesFinder
4. **App-level static files**: Located in `jwql/website/apps/jwql/static/` and automatically discovered

### Directory Structure

```
jwql/website/
├── static/               # Project-level static files (optional, mostly empty)
│   └── css/
│       └── site.css     # Placeholder file
└── apps/
    └── jwql/
        └── static/      # App-level static files (main location)
            ├── css/
            │   ├── bootstrap.min.css
            │   ├── jwql.css
            │   ├── loader.css
            │   ├── loader-magnify.css
            │   └── sticky-footer.css
            ├── js/
            │   ├── jquery-3.3.1.min.js
            │   ├── bootstrap.bundle.min.js
            │   ├── jwql.js
            │   ├── popper.min.js
            │   └── tinysort.min.js
            └── img/
                ├── favicon.ico
                ├── jwql_logo_short_transparent.png
                └── [other images...]
```

## How Static Files Are Served

### In DEBUG Mode (Development)
- Django automatically serves static files from:
  1. Directories listed in `STATICFILES_DIRS`
  2. `static/` subdirectories in each app (via AppDirectoriesFinder)
- No need to run `collectstatic`

### In Production (DEBUG=False)
- Run `python manage.py collectstatic` to copy all static files to `STATIC_ROOT`
- Configure web server (nginx, Apache) to serve files from `STATIC_ROOT`

## AJAX Error Handling

JavaScript functions that make AJAX calls now include error handlers to prevent infinite "Loading..." states:

1. **update_archive_page()**: Shows error message if archive data fails to load
2. **update_thumbnails_page()**: Shows error message if thumbnail data fails to load
3. **update_thumbnails_query_page()**: Shows error message if query data fails to load

Error messages include:
- User-friendly description
- HTTP status information
- Instructions to check browser console
- Suggestion to refresh the page

## Testing Static Files

### Quick Test
Visit: `http://localhost:3001/static-test/`

This page will:
- Display the STATIC_URL configuration
- Load CSS and JavaScript files
- Show which resources loaded successfully
- Display any errors in the browser console

### Manual Testing
1. Start the Django server: `cd jwql/website && python manage.py runserver`
2. Open browser to: `http://localhost:3001/`
3. Open browser DevTools (F12)
4. Check the Network tab for any 404 errors on static files
5. Check the Console tab for JavaScript errors

## Common Issues and Solutions

### Issue: "STATICFILES_DIRS path does not exist"
**Solution**: Settings.py now checks if directories exist before adding them to STATICFILES_DIRS

### Issue: Static files return 404
**Possible causes**:
- DEBUG is set to False (requires collectstatic)
- File path in template doesn't match actual file location
- STATICFILES_FINDERS misconfigured

### Issue: "Loading..." never completes
**Possible causes**:
- AJAX endpoint returns 403/404
- Backend view not implemented
- Database not populated with data
**Solution**: JavaScript now shows error message instead of infinite loading

### Issue: CSS/JS not applying
**Check**:
1. View page source - are the `<link>` and `<script>` tags present?
2. Click the URLs in the tags - do they load?
3. Check browser console for errors
4. Verify file exists in `jwql/website/apps/jwql/static/`

## Server Configuration

### Port Configuration
The server runs on port **3001** by default, configured in `manage.py`:
- Host: 0.0.0.0 (accepts connections from any interface)
- Port: 3001
- Override: `python manage.py runserver 0.0.0.0:8000`

### Running the Server
```bash
cd jwql/website
python manage.py runserver
# Server will start at: http://0.0.0.0:3001/
```

## Relative vs Absolute Paths in AJAX

AJAX calls use `base_url` variable from context to construct full URLs:
```javascript
url: base_url + '/ajax/' + inst + '/archive/',
```

The `base_url` is provided by `get_base_url()` utility function and ensures proper URL construction regardless of deployment environment.

## Debugging Tips

1. **Check Django's static file resolution**:
   ```python
   python manage.py findstatic css/jwql.css
   ```

2. **Enable verbose logging**:
   Add to settings.py:
   ```python
   LOGGING = {
       'version': 1,
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
           },
       },
       'loggers': {
           'django.contrib.staticfiles': {
               'handlers': ['console'],
               'level': 'DEBUG',
           },
       },
   }
   ```

3. **Browser DevTools**:
   - Network tab: See all resource requests and responses
   - Console tab: See JavaScript errors and AJAX failures
   - Elements tab: Inspect loaded CSS styles

## Next Steps

If you continue to see "Loading..." or missing static files:

1. Check that the database is properly initialized
2. Verify that AJAX endpoints are implemented and returning data
3. Ensure filesystem paths in config.json are correct
4. Check that symlinks created by manage.py exist
5. Review browser console for specific error messages
