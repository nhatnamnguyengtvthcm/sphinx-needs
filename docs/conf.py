#
# needs test docs documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 28 11:37:14 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from typing import Any, Dict, List

from sphinx.application import Sphinx

sys.path.append(os.path.abspath("../sphinxcontrib"))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.3"
# The full version, including alpha/beta/rc tags.
release = "1.3.0"

on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    "sphinxcontrib.plantuml",
    "sphinx_needs",
    "sphinx.ext.autodoc",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_copybutton",
    "sphinxcontrib.programoutput",
    "sphinx_design",
    "sphinx.ext.duration",
    "sphinx_immaterial",
]

needs_debug_measurement = True

add_module_names = False  # Used to shorten function name output
autodoc_docstring_signature = True  # Used to read spec. func-defs from docstring (e.g. get rid of self)

NOTE_TEMPLATE = """
.. _{{id}}:

.. note:: {{title}} ({{id}})

   {{content|indent(4) }}

   {% if status -%}
   **status**: {{status}}
   {% endif %}

   {% if tags -%}
   **tags**: {{"; ".join(tags)}}
   {% endif %}

   {% if links -%}
   **links**:
   {% for link in links -%}
       :ref:`{{link}} <{{link}}>` {%if loop.index < links|length -%}; {% endif -%}
   {% endfor -%}
   {% endif %}
"""

EXTRA_CONTENT_TEMPLATE_COLLAPSE = """
.. _{{id}}:

{% if hide == false -%}
.. role:: needs_tag
.. role:: needs_status
.. role:: needs_type
.. role:: needs_id
.. role:: needs_title

.. rst-class:: need
.. rst-class:: need_{{type_name}}

.. dropdown::
   :class: need

            :needs_type:`{{type_name}}`: {% if title %}:needs_title:`{{title}}`{% endif %} :needs_id:`{{id}}`

{% if status and  status|upper != "NONE" and not hide_status %}        | status: :needs_status:`{{status}}`{% endif %}
{% if tags and not hide_tags %}        | tags: :needs_tag:`{{tags|join("` :needs_tag:`")}}`{% endif %}
{% if my_extra_option != "" %}        | my_extra_option: {{ my_extra_option }}{% endif %}
{% if another_option != "" %}        | another_option: {{ another_option }}{% endif %}
        | links incoming: :need_incoming:`{{id}}`
        | links outgoing: :need_outgoing:`{{id}}`

    {{content|indent(4) }}

{% endif -%}
"""

DEFAULT_DIAGRAM_TEMPLATE = (
    "<size:12>{{type_name}}</size>\\n**{{title|wordwrap(15, wrapstring='**\\\\n**')}}**\\n<size:10>{{id}}</size>"
)

# You can uncomment some of the following lines to override the default configuration for Sphinx-Needs.

# needs_template = TITLE_TEMPLATE
# needs_diagram_template = DEFAULT_DIAGRAM_TEMPLATE

# Absolute path to the needs_report_template_file based on the conf.py directory
# needs_report_template = "/needs_templates/report_template.need"   # Use custom report template

needs_types = [
    # Architecture types
    {
        "directive": "int",
        "title": "Interface",
        "content": "plantuml",
        "prefix": "I_",
        "color": "#BFD8D2",
        "style": "card",
    },
    {
        "directive": "comp",
        "title": "Component",
        "content": "plantuml",
        "prefix": "C_",
        "color": "#BFD8D2",
        "style": "card",
    },
    {"directive": "sys", "title": "System", "content": "plantuml", "prefix": "S_", "color": "#BFD8D2", "style": "card"},
    # Normal types
    {"directive": "req", "title": "Requirement", "prefix": "R_", "color": "#BFD8D2", "style": "node"},
    {"directive": "spec", "title": "Specification", "prefix": "S_", "color": "#FEDCD2", "style": "node"},
    {"directive": "impl", "title": "Implementation", "prefix": "I_", "color": "#DF744A", "style": "node"},
    {"directive": "test", "title": "Test Case", "prefix": "T_", "color": "#DCB239", "style": "node"},
    {"directive": "feature", "title": "Feature", "prefix": "F_", "color": "#FFCC00", "style": "node"},
    {"directive": "user", "title": "User", "prefix": "U_", "color": "#777777", "style": "node"},
    {"directive": "action", "title": "Action", "prefix": "A_", "color": "#FFCC00", "style": "node"},
    {"directive": "milestone", "title": "Milestone", "prefix": "M_", "color": "#FF3333", "style": "node"},
]

needs_extra_links = [
    {
        "option": "blocks",
        "incoming": "is blocked by",
        "outgoing": "blocks",
        "copy": True,
        "style": "#AA0000",
        "style_part": "dotted,#AA0000",
        "style_start": "-",
        "style_end": "-o",
        "allow_dead_links": True,
    },
    {
        "option": "tests",
        "incoming": "is tested by",
        "outgoing": "tests",
        "copy": True,
        "style": "#00AA00",
        "style_part": "dotted,#00AA00",
    },
    {
        "option": "checks",
        "incoming": "is checked by",
        "outgoing": "checks",
        "copy": False,
        "style": "#00AA00",
        "style_part": "dotted,#00AA00",
    },
    {
        "option": "triggers",
        "incoming": "triggered by",
        "outgoing": "triggers",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
        "allow_dead_links": True,
    },
    {
        "option": "starts_with",
        "incoming": "triggers directly",
        "outgoing": "starts with",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
    {
        "option": "starts_after",
        "incoming": "triggers at end",
        "outgoing": "starts after",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
    {
        "option": "ends_with",
        "incoming": "triggers to end with",
        "outgoing": "ends with",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
]

needs_flow_configs = {
    "my_config": """
       skinparam monochrome true
       skinparam componentStyle uml2
   """,
    "another_config": """
       skinparam class {
           BackgroundColor PaleGreen
           ArrowColor SeaGreen
           BorderColor SpringGreen
       }
   """,
}

needs_show_link_type = False
needs_show_link_title = False
needs_title_optional = True
needs_max_title_length = 75

needs_id_regex = "^[A-Za-z0-9_]*"
needs_id_required = False
# needs_css = "dark.css"

local_plantuml_path = os.path.join(os.path.dirname(__file__), "utils", "plantuml-1.2022.14.jar")

if on_rtd:
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

# plantuml_output_format = 'png'
plantuml_output_format = "svg_img"

needs_table_style = "datatables"
needs_table_columns = "ID;TITLE;STATUS;OUTGOING"

needs_template_collapse = EXTRA_CONTENT_TEMPLATE_COLLAPSE
needs_extra_options = [
    "my_extra_option",
    "another_option",
    "author",
    "comment",
    "amount",
    "hours",
    "image",
    "config",
    "github",
    "value",
    "unit",
]

needs_warnings = {
    "type_check": 'type not in ["int", "sys", "comp", "req", "spec", "impl", "test", "feature", "action", "user", "milestone", '
    '"issue", "pr", "commit"'  # GitHub service types
    "]",
    # 'valid_status': 'status not in ["open", "in progress", "closed", "done", "implemented"] and status is not None'
}

needs_default_layout = "clean"
needs_default_style = None

needs_layouts = {
    "example": {
        "grid": "simple_side_right_partial",
        "layout": {
            "head": ['**<<meta("title")>>** for *<<meta("author")>>*'],
            "meta": ['**status**: <<meta("status")>>', '**author**: <<meta("author")>>'],
            "side": ['<<image("_images/{{author}}.png", align="center")>>'],
        },
    },
    "permalink_example": {
        "grid": "simple",
        "layout": {
            "head": [
                '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>> <<permalink()>> <<collapse_button("meta", '
                'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=False)>> '
            ],
            "meta": ["<<meta_all(no_links=True)>>", "<<meta_links_all()>>"],
        },
    },
    "detail_view": {
        "grid": "simple",
        "layout": {
            "head": [
                '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>> <<permalink()>> <<collapse_button("meta", '
                'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=False)>> '
                '<<sidebar("")>>'
            ],
            "meta": ["<<meta_all(no_links=True)>>", "<<meta_links_all()>>"],
        },
    },
}

needs_service_all_data = True

needs_services = {
    "github-issues": {
        "url": "https://api.github.com/",
        "max_content_lines": 20,
        "id_prefix": "GH_ISSUE_",
    },
    "github-prs": {
        "url": "https://api.github.com/",
        "max_content_lines": 20,
        "id_prefix": "GH_PR_",
    },
    "github-commits": {
        "url": "https://api.github.com/",
        "max_content_lines": 20,
        "id_prefix": "GH_COM_",
    },
    "open-needs": {
        "url": "http://127.0.0.1:9595",
        "user": os.environ.get("ONS_USERNAME", ""),
        "password": os.environ.get("ONS_PASSWORD", ""),
        "id_prefix": "ONS_",
        "mappings": {
            "id": "{{key}}",
            "type": ["type"],
            "title": "{{title}}",
            "status": ["options", "status"],
            "links": ["references", "links"],
        },
        "extra_data": {
            "Priority": ["options", "priority"],
            "Approval": ["options", "approved"],
            "Cost": ["options", "costs"],
        },
    },
}

needs_string_links = {
    "config_link": {
        "regex": r"^(?P<value>\w+)$",
        "link_url": 'https://sphinxcontrib-needs.readthedocs.io/en/latest/configuration.html#{{value | replace("_", "-")}}',
        "link_name": 'Sphinx-Needs docs for {{value | replace("_", "-") }}',
        "options": ["config"],
    },
    "github_link": {
        "regex": r"^(?P<value>\w+)$",
        "link_url": "https://github.com/useblocks/sphinxcontrib-needs/issues/{{value}}",
        "link_name": "GitHub #{{value}}",
        "options": ["github"],
    },
}


def custom_defined_func():
    return "List of contributors:"


needs_render_context = {
    "custom_data_1": "Project_X",
    "custom_data_2": custom_defined_func(),
    "custom_data_3": True,
    "custom_data_4": [("Daniel", 811982), ("Marco", 234232)],
}

# needs_external_needs = [
#     {
#         "base_url": "https://sphinxcontrib-needs.readthedocs.io/en/latest",
#         "json_path": "examples/needs.json",
#         "id_prefix": "EXT_",
#         "css_class": "external_link",
#     },
# ]

# build needs.json to make permalinks work
needs_build_json = True
# build needs_json for every needs-id to make detail panel
needs_build_json_per_id = False
# Get and maybe set GitHub credentials for services.
# This is needed as the rate limit for not authenticated users is too low for the amount of requests we
# need to perform for this documentation

github_username = os.environ.get("GITHUB_USERNAME", "")
github_token = os.environ.get("GITHUB_TOKEN", "")
if github_username != "" and github_token != "":
    print(f"---> GITHUB: Using as username: {github_username}. length token: {len(github_token)}")
    for service in ["github-issues", "github-prs", "github-commits"]:
        needs_services[service]["username"] = github_username
        needs_services[service]["token"] = github_token
else:
    print("---> GITHUB: No auth provided")

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Sphinx-Needs"
now = datetime.datetime.now()
copyright = f'2017-{now.year}, <a href="http://useblocks.com">team useblocks</a>'
author = "team useblocks"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Control extra excludes like the performance page via env-var.
excludes = os.getenv("SPHINX_EXCLUDE", "").split(",")

exclude_patterns += excludes

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = os.getenv("NEEDS_THEME", "sphinx_immaterial")

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_sidebars = {
    "**": ["about.html", "navigation.html", "searchbox.html"],
}

html_logo = "./_static/sphinx-needs-logo-white.png"
html_favicon = "./_static/sphinx-needs-logo-favicon.png"
# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "site_url": "https://sphinxcontrib-needs.readthedocs.io/",
    "repo_url": "https://github.com/useblocks/sphinxcontrib-needs",
    "repo_name": "Sphinx-Needs",
    "repo_type": "github",
    "edit_uri": "blob/master/docs",
    # "google_analytics": ["UA-XXXXX", "auto"],
    "globaltoc_collapse": True,
    "features": [
        "navigation.sections",
        "navigation.top",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "accent": "yellow",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "needstestdocsdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements: Dict[str, Any] = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "needstestdocs.tex", "needs test docs Documentation", "team useblocks", "manual"),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "needstestdocs", "needs test docs Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "needstestdocs",
        "needs test docs Documentation",
        author,
        "needstestdocs",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# contains different constraints
needs_constraints = {
    "critical": {"check_0": "'critical' in tags", "check_1": "'SECURITY_REQ' in links", "severity": "CRITICAL"},
    "security": {"check_0": "'security' in tags", "severity": "HIGH"},
    "team": {"check_0": 'author == "Bob"', "severity": "LOW"},
}

# defines what to do if a constraint is not met
needs_constraint_failed_options = {
    "CRITICAL": {"on_fail": ["warn"], "style": ["red_bar"], "force_style": True},
    "HIGH": {"on_fail": ["warn"], "style": ["orange_bar"], "force_style": True},
    "MEDIUM": {"on_fail": ["warn"], "style": ["yellow_bar"], "force_style": False},
    "LOW": {"on_fail": [], "style": ["yellow_bar"], "force_style": False},
}

# variants options
needs_variant_options = ["status"]

rst_epilog = """
.. |ex| replace:: **Example**

.. |out| replace:: **Result**

.. |br| raw:: html

   <br>

"""

# Check, if docs get built on ci.
# If this is the case, external services like Open-Needs are not available and
# docs will show images instead of getting real data.
on_ci = os.environ.get("ON_CI", "False").upper() == "TRUE"
fast_build = os.environ.get("FAST_BUILD", "False").upper() == "TRUE"

html_context = {"on_ci": on_ci, "fast_build": fast_build}


def rstjinja(app: Sphinx, _docname: str, source: List[str]) -> None:
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != "html" and app.builder.name != "linkcheck":
        return
    src = source[0]
    from jinja2 import Template

    template = Template(src, autoescape=True)
    rendered = template.render(**app.config.html_context)
    source[0] = rendered


def setup(app: Sphinx) -> None:
    print(f"---> ON_CI is: {on_ci}")
    print(f"---> FAST_BUILD is: {fast_build}")
    app.connect("source-read", rstjinja)


# LINKCHECK config
# https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=linkcheck#options-for-the-linkcheck-builder
linkcheck_ignore = [
    r"http://localhost:\d+",
    r"http://127.0.0.1:\d+",
    r"../.*",
]

linkcheck_request_headers = {
    "*": {
        "User-Agent": "Mozilla/5.0",
    }
}

linkcheck_workers = 5
