# Documentation for PiPico W training

## About

Sphinx generate documentation in the preferred formats of your audience,
including HTML, LaTeX (for PDF), ePub, Texinfo, and [more](https://www.sphinx-doc.org/en/master/index.html#).

### Sphinx workflow

Github workflow for creating Sphinx docs can be found [here](https://github.com/ikostan/pico/blob/master/.github/workflows/sphinx_docs.yml).

### Install Sphinx from PyPI package

Sphinx packages are published on the Python Package Index (PyPI).
The preferred tool for installing packages from PyPI is pip, which is
included in all modern versions of Python.

1. Open CMD
2. Run:
```
 python -m pip install -U sphinx
 python -m pip install sphinx_rtd_theme
 python -m pip install --upgrade myst-parser
 python -m pip install commonmark
 python -m pip install docutils
```

### Check Sphinx version

1. Open CMD
2. Run:
```
python -m sphinx-build --version
python -m sphinx-quickstart --version
```

### Check whether MyST parser is available

1. Open CMD
2. Run: ```python -c "import myst_parser"```

### Sphinx build

1. Open CMD
2. Run: ```python -m sphinx-build docs docs/_build --verbose```

### Auto-Generated Python Documentation with Sphinx

Step by step:

1. Open CMD
2. Go to docs directory
3. Run: ```make clean```
4. Run: ```sphinx-apidoc -F -P -o . ..```
5. Add doc files name into relevant doc rst file
6. Run: ```make html```

### Online Documentation

Tech documentation is available [here](https://ikostan.github.io/pico/).
