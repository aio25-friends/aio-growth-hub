# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AIO2025 | Share Value Together'
copyright = '2025, AIO FRIENDS GROUP'
author = 'AIO Friends Group'
release = '1.0'
html_title = author # Change display name in sidebar to 'author'

import sys
print("TEMPLATES PATHS LOADED:", sys.path)

# import os
# print("LOOKING FOR TEMPLATES AT:", os.path.abspath("_templates"))
# print("FULL FILE EXISTS:", os.path.exists("_templates/page.html"))

import jinja2
jinja2.debug = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
#    'sphinx_gallery.gen_gallery',
#    'pyvista.ext.plot_directive',
    'myst_parser',
    'nbsphinx',
    'sphinx.ext.githubpages',
]

html_context = {
    "display_github": True,
    "github_user": "ai-thutam89",  # ✏️ Your GitHub username
    "github_repo": "ai-learning-journey",  # ✏️ Your repository name
    "github_version": "main",  # Branch
    "doc_path": "source",  # Folder where your .rst files are
}

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

epub_enabled = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Default theme : alabaster
html_theme = 'furo'
html_static_path = ['_static']

html_css_files = ['custom.css']
html_js_files = ['custom.js']

# html_favicon = "_static/favicon.ico"

html_theme_options = {
    "sidebar_hide_name": False,         # Show project name/logo in sidebar
    "navigation_with_keys": True,       # Enable keyboard navigation

    "source_repository": "https://github.com/pradyunsg/furo/",
    "source_branch": "main",
    "source_directory": "docs/source/",
}