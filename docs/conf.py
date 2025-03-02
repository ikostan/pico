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
copyright = '2025, Egor Kostan'
author = 'Egor Kostan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.duration',
              'sphinx.ext.coverage',
              'sphinx.ext.todo',
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
# html_theme = 'sphinx_rtd_theme'

# PDJ Theme
# https://sphinx-themes.org/sample-sites/sphinx-pdj-theme/
# html_theme = 'sphinx_pdj_theme'
html_theme = 'furo'
html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

# Source:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path
html_static_path = ['_static',
                    '_static/.htaccess']

source_suffix = {'.rst': 'restructuredtext',
                 '.md': 'markdown'}

# Different logos for light and dark mode
# https://pradyunsg.me/furo/customisation/logo/
html_theme_options = {
    "light_logo": "logo-light-mode.png",
    "dark_logo": "logo-dark-mode.png",
}
