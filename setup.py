# -*- coding: utf-8 -*-
#
# This file is part of RERO ILS.
# Copyright (C) 2017 RERO.
#
# RERO ILS is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# RERO ILS is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RERO ILS; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio digital library framework."""

import os

from setuptools import find_packages, setup
from setuptools.command.egg_info import egg_info


class EggInfoWithCompile(egg_info):
    def run(self):
        from babel.messages.frontend import compile_catalog
        compiler = compile_catalog()
        option_dict = self.distribution.get_option_dict('compile_catalog')
        if option_dict.get('domain'):
            compiler.domain = [option_dict['domain'][1]]
        else:
            compiler.domain = ['messages']
        compiler.use_fuzzy = True
        compiler.directory = option_dict['directory'][1]
        compiler.run()
        super().run()


readme = open('README.rst').read()

INVENIO_VERSION = "3.0.0"

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('rero_ils', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    cmdclass={
        'egg_info': EggInfoWithCompile
    },
    name='rero-ils',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='rero-ils Invenio',
    license='GPL',
    author='RERO',
    author_email='software@rero.ch',
    url='https://github.com/rero/rero-ils',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'rero-ils = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            # 'flask_debugtoolbar = flask_debugtoolbar:DebugToolbarExtension',
            'rero-ils = rero_ils.modules.ext:REROILSAPP'
        ],
        'invenio_base.blueprints': [
            'rero_ils = rero_ils.views:blueprint',
            'organisations =\
                rero_ils.modules.organisations_members.views:blueprint',
            'members = rero_ils.modules.members_locations.views:blueprint',
            'locations = rero_ils.modules.locations.views:blueprint',
            'documents_items =\
                rero_ils.modules.documents_items.views:blueprint',
            'documents = rero_ils.modules.documents.views:blueprint',
            'items = rero_ils.modules.items.views:blueprint',
            'patrons = rero_ils.modules.patrons.views:blueprint',
        ],
        'invenio_config.module': [
            'rero_ils = rero_ils.config',
        ],
        'invenio_i18n.translations': [
            'messages = rero_ils',
        ],
        'invenio_assets.bundles': [
            'rero_ils_search_js = rero_ils.bundles:search_js',
            'rero_ils_item_editor_js =\
                rero_ils.modules.items.bundles:editor_js',
            'rero_ils_item_circulation_ui_js =\
                rero_ils.modules.items.bundles:circulation_ui_js',
            'rero_ils_document_editor_js =\
                rero_ils.modules.documents.bundles:editor_js',
            'rero_ils_patron_profile_css =\
                rero_ils.modules.patrons.bundles:profile_css',
            'rero_ils_patron_editor_js =\
                rero_ils.modules.patrons.bundles:editor_js',
            'rero_ils_member_editor_js =\
                rero_ils.modules.members_locations.bundles:editor_js',
            'rero_ils_location_editor_js =\
                rero_ils.modules.locations.bundles:editor_js'
        ],
        'dojson.cli': [
            'reverse = rero_ils.dojson.cli:reverse',
            'head = rero_ils.dojson.cli:head',
        ],
        'dojson.cli.dump': [
            'pjson = rero_ils.modules.dojson.dump:pretty_json_dump',
        ],
        'dojson.cli.rule': [
            'marc21tojson =\
                rero_ils.modules.documents.dojson.contrib.marc21tojson:marc21tojson',
            'marc21toebooks =\
                rero_ils.modules.ebooks.dojson.contrib.marc21:marc21',
            'unimarctojson =\
                rero_ils.modules.documents.dojson.contrib.unimarctojson:unimarctojson',
        ],
        'flask.commands': [
            'fixtures = rero_ils.modules.cli:fixtures',
            'utils = rero_ils.modules.cli:utils',
            'oaiharvester = rero_ils.modules.ebooks.cli:oaiharvester'
        ],
        'invenio_db.models': [
            'organisations = rero_ils.modules.organisations.models',
            'organisations_members =\
                rero_ils.modules.organisations_members.models',
            'members = rero_ils.modules.members.models',
            'members_locations = rero_ils.modules.members_locations.models'
            'locations = rero_ils.modules.locations.models',
            'documents = rero_ils.modules.documents.models',
            'documents_items = rero_ils.modules.documents_items.models',
            'items = rero_ils.modules.items.models',
            'patrons = rero_ils.modules.patrons.models',
            'transactions = rero_ils.modules.transactions.models',
        ],
        'invenio_pidstore.minters': [
            'organisation_id =\
                rero_ils.modules.organisations.minters:organisation_id_minter',
            'member_id =\
                rero_ils.modules.members.minters:member_id_minter',
            'location_id =\
                rero_ils.modules.locations.minters:location_id_minter',
            'document_id =\
                rero_ils.modules.documents.minters:document_id_minter',
            'item_id = rero_ils.modules.items.minters:item_id_minter',
            'patron_id = rero_ils.modules.patrons.minters:patron_id_minter',
        ],
        'invenio_pidstore.fetchers': [
            'organisation_id =\
                rero_ils.modules.organisations.fetchers:organisation_id_fetcher',
            'member_id =\
                rero_ils.modules.members.fetchers:member_id_fetcher',
            'location_id =\
                rero_ils.modules.locations.fetchers:location_id_fetcher',
            'document_id =\
                rero_ils.modules.documents.fetchers:document_id_fetcher',
            'item_id =\
                rero_ils.modules.items.fetchers:item_id_fetcher',
            'patron_id =\
                rero_ils.modules.patrons.fetchers:patron_id_fetcher',
        ],
        'invenio_jsonschemas.schemas': [
            'organisations = rero_ils.modules.organisations.jsonschemas',
            'members = rero_ils.modules.members.jsonschemas',
            'locations = rero_ils.modules.locations.jsonschemas',
            'documents = rero_ils.modules.documents.jsonschemas',
            'items = rero_ils.modules.items.jsonschemas',
            'patrons = rero_ils.modules.patrons.jsonschemas',
        ],
        'invenio_search.mappings': [
            'organisations = rero_ils.modules.organisations.mappings',
            'members = rero_ils.modules.members.mappings',
            'locations = rero_ils.modules.locations.mappings',
            'documents = rero_ils.modules.documents.mappings',
            'items = rero_ils.modules.items.mappings',
            'patrons = rero_ils.modules.patrons.mappings',
        ],
        'invenio_celery.tasks': [
            'rero_ils_oaiharvest = rero_ils.modules.ebooks.tasks',
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
