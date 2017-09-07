#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Python España'
SITENAME = 'Python España'
SITEURL = ''
SITESUBTITLE = 'Web de la Asociación'
SITEIMAGE = '/images/logo.png'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
ICONS = (
    ('twitter', 'https://twitter.com/python_es'),
    ('github', 'https://github.com/python-spain'),
    ('youtube', 'https://www.youtube.com/Python-España'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-alchemy/alchemy'

STATIC_PATHS = ['images']
