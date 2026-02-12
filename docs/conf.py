# docs/conf.py
project = 'Emerald'
copyright = '2026, Gem Creative'
author = 'Gem Creative'

extensions = [
    'myst_parser',
    'sphinx_copybutton',
]

html_theme = 'furo'

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2ecc71",
        "color-brand-content": "#27ae60",
    },
    "dark_css_variables": {
        "color-brand-primary": "#2ecc71",
        "color-brand-content": "#2ecc71",
        "color-sidebar-background": "#121212",
    },
}

html_logo = "_static/emer.png"
html_favicon = "_static/emer.png"
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = []

