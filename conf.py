# -*- coding: utf-8 -*-
#
# rosindex documentation build configuration file, created by
# sphinx-quickstart on Tue Oct  2 16:34:57 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import itertools
import os
import sys
import time

from docutils.parsers.rst import Directive

sys.path.append(os.path.abspath('./sphinx-multiversion'))


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# The master toctree document.
master_doc = 'index'

# The default role
default_role = 'any'

# The set of warnings to suppress.
suppress_warnings = ['image.nonlocal_uri']

# General information about the project.
project = 'ROS 2 documentation'
author = 'Open Robotics'
copyright = '{}, {}'.format(time.strftime('%Y'), author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# Define the default role to use for links
default_role = 'any'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['**/_*.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
extensions = ['sphinx.ext.intersphinx', 'sphinx_tabs.tabs', 'sphinx_multiversion', 'sphinx_rtd_theme']

# Intersphinx mapping

intersphinx_mapping = {
    'catkin_pkg':    ('http://docs.ros.org/en/independent/api/catkin_pkg/html', None),
    'jenkins_tools': ('http://docs.ros.org/en/independent/api/jenkins_tools/html', None),
    'rosdep':        ('http://docs.ros.org/en/independent/api/rosdep/html', None),
    'rosdistro':     ('http://docs.ros.org/en/independent/api/rosdistro/html', None),
    'rosinstall':    ('http://docs.ros.org/en/independent/api/rosinstall/html', None),
    'rospkg':        ('http://docs.ros.org/en/independent/api/rospkg/html', None),
    'vcstools':      ('http://docs.ros.org/en/independent/api/vcstools/html', None)
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
}

html_context = {
    'display_github': True,
    'github_user': 'ros2',
    'github_repo': 'ros2_documentation',
    'github_version': 'rolling/source/',  # Will be overridden when building multiversion
}

templates_path = [
    "source/_templates",
]

# smv_tag_whitelist = None

smv_branch_whitelist = r'^(rolling|foxy|eloquent|dashing|crystal)$'


smv_released_pattern = r'^refs/(heads|remotes/[^/]+)/(foxy|eloquent|dashing|crystal).*$'
smv_remote_whitelist = r'^(origin)$'
smv_latest_version = 'foxy'



html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Drop any source link suffix
html_sourcelink_suffix = ''

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ros2_docsdoc'

html_baseurl = 'https://docs.ros.org/en'

class RedirectFrom(Directive):

    has_content = True
    template_name = 'layout.html'
    redirections = {}

    @classmethod
    def register(cls, app):
        app.connect('html-collect-pages', cls.generate)
        app.add_directive('redirect-from', cls)
        return app

    @classmethod
    def generate(cls, app):
        from sphinx.builders.html import StandaloneHTMLBuilder
        if not isinstance(app.builder, StandaloneHTMLBuilder):
            return

        redirect_html_fragment = """
            <link rel="canonical" href="{base_url}/{url}" />
            <meta http-equiv="refresh" content="0; url={url}" />
            <script>
                window.location.href = '{url}';
            </script>
        """
        redirections = {
            os.path.splitext(os.path.relpath(
                document_path, app.srcdir
            ))[0]: redirect_urls
            for document_path, redirect_urls in cls.redirections.items()
        }
        redirection_conflict = next((
            (canon_1, canon_2, redirs_1.intersection(redirs_2))
            for (canon_1, redirs_1), (canon_2, redirs_2)
            in itertools.combinations(redirections.items(), 2)
            if redirs_1.intersection(redirs_2)
        ), None)
        if redirection_conflict:
            canonical_url_1, canonical_url_2 = redirection_conflict[:2]
            conflicting_redirect_urls = redirection_conflict[-1]
            raise RuntimeError(
                'Documents {} and {} define conflicting redirects: {}'.format(
                    canonical_url_1, canonical_url_2, conflicting_redirect_urls
                )
            )
        all_canonical_urls = set(redirections.keys())
        all_redirect_urls = {
            redirect_url
            for redirect_urls in redirections.values()
            for redirect_url in redirect_urls
        }
        conflicting_urls = all_canonical_urls.intersection(all_redirect_urls)
        if conflicting_urls:
            raise RuntimeError(
                'Some redirects conflict with existing documents: {}'.format(
                    conflicting_urls
                )
            )

        for canonical_url, redirect_urls in redirections.items():
            for redirect_url in redirect_urls:
                context = {
                    'canonical_url': os.path.relpath(
                        canonical_url, redirect_url
                    ),
                    'title': os.path.basename(redirect_url),
                    'metatags': redirect_html_fragment.format(
                        base_url=app.config.html_baseurl,
                        url=app.builder.get_relative_uri(
                            redirect_url, canonical_url
                        )
                    )
                }
                yield (redirect_url, context, cls.template_name)

    def run(self):
        document_path = self.state.document.current_source
        if document_path not in RedirectFrom.redirections:
            RedirectFrom.redirections[document_path] = set()
        RedirectFrom.redirections[document_path].update(self.content)
        return []


def make_router(origin, destination):
    def _missing_reference(app, env, node, contnode):
        from docutils import nodes
        from docutils.utils import relative_path
        from sphinx.util import docname_join

        doctarget = docname_join(node['refdoc'], node['reftarget'])
        if doctarget.startswith(origin):
            routed_doctarget = doctarget.replace(origin, destination)
            if routed_doctarget in env.all_docs:
                newnode = nodes.reference(
                    '', contnode.astext(), internal=True
                )
                newnode['refuri'] = app.builder.get_relative_uri(
                    node['refdoc'], routed_doctarget
                )
                return newnode
    return _missing_reference

def smv_rewrite_configs(app, config):
    # When using Sphinx multiversion, there is no way at initial configuration time
    # to determine the distribution we are currently targeting (conf.py is read before
    # external defines are setup, and environment variables aren't passed through to
    # conf.py).  Instead, hook into the 'config-inited' event which is late enough
    # to rewrite the various configuration items with the current version.
    if app.config.smv_current_version != '':
        app.config.html_baseurl = app.config.html_baseurl + '/' + app.config.smv_current_version
        app.config.project = 'ROS 2 Documentation: ' + app.config.smv_current_version.title()

        if app.config.smv_current_version != 'rolling':
            app.config.html_logo = 'source/Releases/' + app.config.smv_current_version + '-small.png'

def github_link_rewrite_branch(app, pagename, templatename, context, doctree):
    if app.config.smv_current_version != '':
        context['github_version'] = app.config.smv_current_version + '/source/'

def setup(app):
    app.connect('config-inited', smv_rewrite_configs)
    app.connect('html-page-context', github_link_rewrite_branch)
    RedirectFrom.register(app)
