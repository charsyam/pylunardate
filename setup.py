#!/usr/bin/env python

from setuptools import setup, find_packages

DESCRIPTION = """Python Lunar Calendar
"""

setup(name='pylunardate',
      version='0.0.3',
      packages=['lunardate'],
      description = 'A Korean Calendar Library in Pure Python',
	    long_description=DESCRIPTION,
      author = 'charsyam',
      author_email = 'charsyam@gmail.com',
      url = 'https://github.com/charsyam/pylunardate',
      license = 'BSD',
      classifiers = [
                     'Development Status :: 4 - Beta',
                     'Programming Language :: Python',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
			               'Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Topic :: Software Development :: Libraries'
                     ]
      )
