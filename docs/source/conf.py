# -*- coding: utf-8 -*-
#
# import os
# import sys
# sys.path.append(os.path.abspath('_extensions'))


# -- Project information -----------------------------------------------------

project = 'KDHUT'
#copyright = 'GMS'
author = 'Kirsten & Dani'

# The full version, including alpha/beta/rc tags
# release = '2019'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# Install Bibtex ext. using pip install sphinxcontrib-bibtex
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages'
#				'sphinx_multiversion',
#				'sphinxcontrib.bibtex',
#				'sphinx.ext.mathjax',
#				'sphinx_inline_tabs',
	#			'sphinx_rtd_theme',
]

# Rst2pdf index page generator
# pdf_documents = [('index', u'rst2pdf', u'RST2PDF', u'KI'),]

# BibTex Library pointer
#bibtex_bibfiles = ['refs.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Start auto numbering of figure and tables
numfig = True
# Numbering as Fig 1., increase depth to incude section numbers as well
numfig_secnum_depth = 0

# Start eqn numbering
math_numfig = True
math_eqref_format = '({number})'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    #'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_logo="_static/logo/hut.png"
# some customized css style
html_css_files = ["style.css"]

# show/hide 'Page Source' Link
html_show_sourcelink = False
