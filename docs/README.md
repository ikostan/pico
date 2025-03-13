# Documentation for PiPico W training

![Sphinx Logo](https://github.com/ikostan/pico/blob/master/img/sphinxdoclogo.png)

## About

Sphinx generate documentation in the preferred formats of your audience,
including HTML, LaTeX (for PDF), ePub, Texinfo, and [more](https://www.sphinx-doc.org/en/master/index.html#).

### Sphinx workflow

Github workflow for creating Sphinx docs can be found [here](https://github.com/ikostan/pico/blob/master/.github/workflows/sphinx_docs.yml).

---
### How to instructions...

<details>
  <summary>Install Sphinx from PyPI package</summary>
<br>
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

<details>
  <summary>Check Sphinx version</summary>
<br>
1. Open CMD
2. Run:

```bash
sphinx-build --version
sphinx-quickstart --version
```
</details>

<details>
  <summary>Check whether MyST parser is available</summary>
<br>
1. Open CMD
2. Run: 

```bash
python -c "import myst_parser"
```
</details>

<details>
  <summary>Defining document structure</summary>
<br>
Sphinx comes with a script called sphinx-quickstart that sets up a source
directory and creates a default conf.py with the most useful configuration
values from a few questions it asks you.

1. Open CMD:
2. Run:

```bash
sphinx-quickstart
```
</details>

<details>
  <summary>Sphinx build</summary>
<br>
1. Open CMD
2. Run:

```bash
sphinx-build docs docs/_build --verbose
```
</details>

<details>
  <summary>Auto-Generated Python Documentation with Sphinx</summary>
<br>
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
</details>

<details>
  <summary>Furo theme</summary>
<br>
A clean customisable Sphinx documentation theme.

Furo is distributed on PyPI. To use the theme in your Sphinx project:

1. Install Furo in documentation’s build environment.
```bash
pip install furo
```
2. Update the html_theme in `conf.py`.
```bash
html_theme = "furo"
```
3. Your Sphinx documentation’s HTML pages will now be generated with this theme!

[Source](https://pradyunsg.me/furo/)
</details>

<details>
  <summary>Markdown support</summary>
<br>
To configure your Sphinx project for Markdown support, proceed as follows:

1. Install the Markdown parser MyST-Parser:
```bash
pip install --upgrade myst-parser
```
2. Add myst_parser to the list of configured extensions:
```bash
extensions = ['myst_parser']
```
3. If you want to use Markdown files with extensions other than .md, 
   adjust the source_suffix variable. The following example configures
   Sphinx to parse all files with the extensions .md and .txt as Markdown:
```bash
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
```
4. You can further configure MyST-Parser to allow custom syntax that 
   standard CommonMark doesn’t support. Read more in the MyST-Parser documentation.

[Source](https://www.sphinx-doc.org/en/master/usage/markdown.html)
</details>

---
### Online Documentation

Detailed tech documentation is available [here](https://ikostan.github.io/pico/).

### Source list

- [Sphinx](https://www.sphinx-doc.org/en/master/index.html)
- [Fix missing images when using include directives](https://stackoverflow.com/questions/50261137/docs-missing-images-when-using-include-directives-rst-sphinx)
- [Intro to Documentation with Sphinx and reStructuredText’s documentation](https://sphinx-intro-tutorial.readthedocs.io/en/latest/index.html)
