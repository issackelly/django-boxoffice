from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name='django-boxoffice',
    version="0.2.0-dev",
    package_dir={'boxoffice': 'boxoffice'},
    package_data={'blogdor': ['templates/boxoffice/*.html']},
    packages=['boxoffice'],
    description='Django ticket registration application',
    author='James Turk',
    author_email='jturk@sunlightfoundation.com',
    license='BSD License',
    url='http://github.com/sunlightlabs/django-boxoffice/',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
