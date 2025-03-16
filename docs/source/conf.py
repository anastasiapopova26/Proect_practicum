import os
import sys

project = 'Autodoc'
copyright = '2025, Popova A. M.'
author = 'Popova A. M.'
release = '1'

sys.path.insert(0, os.path.abspath('../dash_app'))
sys.path.insert(0, os.path.abspath('../app'))
sys.path.insert(0, os.path.abspath('../playwright-project'))

extensions = [
    'sphinx.ext.autodoc'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
