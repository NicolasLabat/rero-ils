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

"""Fetchers module tests."""

from __future__ import absolute_import, print_function

from uuid import uuid4

from rero_ils.modules.patrons.fetchers import patron_id_fetcher as fetcher
from rero_ils.modules.patrons.minters import patron_id_minter as minter


def test_patron_id_fetcher(db):
    """Test patron_id fetcher."""
    data = {}
    rec_uuid = uuid4()
    minted_pid = minter(rec_uuid, data)
    fetched_pid = fetcher(rec_uuid, data)

    assert minted_pid.pid_value == fetched_pid.pid_value
    assert fetched_pid.pid_type == fetched_pid.provider.pid_type
    assert fetched_pid.pid_type == 'ptrn'
