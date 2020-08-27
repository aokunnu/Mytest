#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ayo Okunnu'
SITENAME = 'My First Site'
SITEURL = ''
SITESUBTITLE = 'Site Subtitle'
PATH = 'content'
TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'themes/Peli-Kiera'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']
STATIC_PATHS = ['images']
SUMMARY_MAX_LENGTH = 60
DEFAULT_PAGINATION = 10
GITHUB_URL = 'https://github.com/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True

# Social widget
SOCIAL = (
            ('twitter', 'https://twitter.com/'),
                ('linkedin', 'https://www.linkedin.com'),
                    ('github', 'https://github.com/'),
                        ('gitlab', 'https://gitlab.com/'),
                            ('facebook', 'https://facebook.com'),
                                ('instagram', 'https://instagram.com'),
                                )

# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
