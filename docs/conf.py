# pylint: skip-file

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import pathlib
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
              'sphinx.ext.mathjax',]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Include README.md in sphinx documentation
# Source:
# https://www.lieret.net/2021/05/20/include-readme-sphinx/

# My current workaround is to add the following in conf.py:

# Add recommonmark to the list of extensions
# Set source_suffix = [".rst", ".md"]
# Add the following snippet:

source_suffix = [".rst", ".md"]

# The readme that already exists
path = '../README.md'
readme_path = pathlib.Path(path).parent.resolve().parent / "README.md"

# We copy a modified version here
readme_target = pathlib.Path(path).parent / "readme.md"

# Change the title to "Readme"
with readme_target.open("w") as outf:
    outf.write(
        "\n".join(
            ["Readme",
             "======",])
    )
    lines = []
    for line in readme_path.read_text().split("\n"):
        # Skip title, because we now use "Readme"
        # Could also simply exclude first line for the same effect
        if line.startswith("# "):
            continue
        lines.append(line)
    outf.write("\n".join(lines))
