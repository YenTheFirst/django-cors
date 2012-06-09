django-cors
===========

A Django app for handling Cross-Origin Resource Sharing.

Install by cloning the repo and running

::

    sudo python setup.py install

Then add the app to the installed apps in your settings file::

    INSTALLED_APPS = (
        # ...
        'cors',
        # ...
    )

To allow requests to be made from the browser from cross domains, use ``AllowOriginMiddleware``::

    MIDDLEWARE_CLASSES = (
        # ...
        'cors.middleware.AllowOriginMiddleware',
        # ...
    )

and then set ALLOWED_CROSS_DOMAIN_ORIGINS::

    #all_origins
    ALLOWED_CROSS_DOMAIN_ORIGINS = '*'

    #just two subdomains of example.com
    ALLOWED_CROSS_DOMAIN_ORIGINS = [
        'http://subdomain1.example.com',
        'http://subdomain2.exapmle.com',
    ]

    #only a single domain
    ALLOWED_CROSS_DOMAIN_ORIGINS = 'http://example.com'

cross-domain cookies and credentials can be set with::

    ALLOWED_CROSS_DOMAIN_CREDENTIALS = true
