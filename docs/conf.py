"""Sphinx configuration."""
project = "Dogg Biscuit"
author = "wcDogg"
copyright = "2022, wcDogg"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
