# Documentation for PiPico W training

![Sphinx Logo](https://github.com/ikostan/pico/blob/master/img/sphinxdoclogo.png)

## About

Sphinx generate documentation in the preferred formats of your audience,
including HTML, LaTeX (for PDF), ePub, Texinfo, and [more](https://www.sphinx-doc.org/en/master/index.html#).

### Sphinx workflow

Github workflow for creating Sphinx docs can be found [here](https://github.com/ikostan/pico/blob/master/.github/workflows/sphinx_docs.yml).

<details>
  <summary>Install Sphinx from PyPI package</summary>

Sphinx packages are published on the Python Package Index (PyPI).
The preferred tool for installing packages from PyPI is pip, which is
included in all modern versions of Python.

1. Open CMD
2. Run:

```bash
 python -m pip install -U sphinx
 python -m pip install sphinx_rtd_theme
 python -m pip install --upgrade myst-parser
 python -m pip install commonmark
 python -m pip install docutils
```
</details>

### Check Sphinx version

1. Open CMD
2. Run:

```bash
sphinx-build --version
sphinx-quickstart --version
```

### Check whether MyST parser is available

1. Open CMD
2. Run: 

```bash
python -c "import myst_parser"
```

### Defining document structure

Sphinx comes with a script called sphinx-quickstart that sets up a source
directory and creates a default conf.py with the most useful configuration
values from a few questions it asks you.

1. Open CMD:
2. Run:

```bash
sphinx-quickstart
```

### Sphinx build

1. Open CMD
2. Run:

```bash
sphinx-build docs docs/_build --verbose
```

### Auto-Generated Python Documentation with Sphinx

Step by step:

- Open CMD
- Go to `docs` directory
- Run:

```bash 
make clean
```

- Run: 

```bash
sphinx-apidoc -F -P -o . ..
```

- Add doc files name into relevant doc rst file
- Run: 

```bash
make html
```

### Online Documentation

Tech documentation is available [here](https://ikostan.github.io/pico/).

### Source list

- [Sphinx](https://www.sphinx-doc.org/en/master/index.html)
- [Fix missing images when using include directives](https://stackoverflow.com/questions/50261137/docs-missing-images-when-using-include-directives-rst-sphinx)
