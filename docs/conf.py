# pylint: skip-file

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PiPico W Training'
copyright = '2024, Egor Kostan'
author = 'Egor Kostan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.autodoc',
              'sphinx.ext.mathjax',
              'myst_parser']

templates_path = ['_templates']

exclude_patterns = ['_build',
                    'Thumbs.db',
                    '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# Source:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path
html_static_path = ['_static',
                    '_static/.htaccess']

source_suffix = {'.rst': 'restructuredtext',
                 '.md': 'markdown'}
