# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If your extensions or modules to document with autodoc are in another directory,
# add those directories here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate Netflix on Your Smart TV'
copyright = '2025, Activate Netflix Guide'
author = 'Activate Netflix Guide'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Activate Netflix on Your Smart TV – Easy Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Activate Netflix Guide"

# Favicon (place your favicon.ico file in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (you can uncomment to use sphinx_rtd_theme if installed)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source" link at bottom of pages
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files (needed for your buttons and custom HTML)
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Enable raw HTML directives
raw_enabled = True

# Paths to templates and static files
# templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you add static assets like CSS or images

# Patterns to exclude from source file discovery
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
