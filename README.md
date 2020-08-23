# Desk Auth

Desk Auth is a Django user authentication application based on
the standard Django authentication application with some improvements.

Detailed documentation is in the "docs" directory.

Quick start
-----------
- Add "desk-auth" to your INSTALLED_APPS setting like this:
```
INSTALLED_APPS = [
    ...
    'desk_auth',
]
```
- Run ``python manage.py migrate`` to create the polls models.

- Start the development server and visit http://127.0.0.1:8000/admin/ 
  to create a poll (you'll need the Admin app enabled).


