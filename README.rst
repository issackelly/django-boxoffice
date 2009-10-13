================
django-boxoffice
================

Django event registration application.

django-boxoffice is a project of Sunlight Labs (c) 2009.
Written by James Turk <jturk@sunlightfoundation.com>

Source: http://github.com/sunlightlabs/django-boxoffice/

Requirements
============

python >= 2.4

django >= 1.0

Installation
============

To install run 

    ``python setup.py install``

which will install the application into the site-packages directory.

Usage
=====

Configuration
-------------

#.  Add ``boxoffice`` to INSTALLED_APPS
#.  Include ``boxoffice.urls`` to urls.py (eg. ``url(r'^tickets/', include('boxoffice.urls')),``)

Templates
---------

Three templates are used by django-boxoffice:
    * boxoffice/attendee_list.html
    * boxoffice/registration_form.html
    * boxoffice/registration_table.html

Example templates are provided, any or all may be overriden in the usual manner.
