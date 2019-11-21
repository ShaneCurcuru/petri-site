#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

import sys
import os


AUTHOR = u'PetriCommunity'
SITENAME = u'Apache Petri'
SITEURL = ''
CURRENTYEAR = date.today().year

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'
SITEURL = 'https://petri.apache.org'

# Save pages using full directory preservation
PATH_METADATA= '(?P<path_no_ext>.*)\..*'
PAGE_SAVE_AS= '{path_no_ext}.html'
PAGE_URL= '{path_no_ext}.html'

# Standard behavior:
#PAGE_SAVE_AS = './{slug}.html'

ARTICLE_SAVE_AS = 'news/{slug}.html'
ARTICLE_URL = 'news/{slug}.html'

# Sort news by date, descending, latest article first
ARTICLE_ORDER_BY = 'reversed-date'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# TOC Generator
PLUGIN_PATHS = ['./theme/plugins']
PLUGINS = ['toc']
TOC_HEADERS = r"h[1-6]"

# Unused links
LINKS = ( )
SOCIAL = ( )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
