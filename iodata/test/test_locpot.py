# -*- coding: utf-8 -*-
# HORTON: Helpful Open-source Research TOol for N-fermion systems.
# Copyright (C) 2011-2017 The HORTON Development Team
#
# This file is part of HORTON.
#
# HORTON is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# HORTON is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --
# pragma pylint: disable=invalid-name
"""Test iodata.locpot module."""


from .. utils import angstrom, electronvolt, volume
from .. iodata import IOData
try:
    from importlib_resources import path
except ImportError:
    from importlib.resources import path


def test_load_locpot_oxygen():
    with path('iodata.test.cached', 'LOCPOT.oxygen') as fn:
        mol = IOData.from_file(str(fn))
    assert mol.title == 'O atom in a box'
    assert (mol.numbers[0] == [8]).all()
    assert abs(volume(mol.rvecs) - (10 * angstrom) ** 3) < 1e-10
    ugrid = mol.grid
    assert len(ugrid['shape']) == 3
    assert (ugrid['shape'] == [1, 4, 2]).all()
    assert abs(ugrid['origin']).max() < 1e-10
    d = mol.cube_data
    assert abs(d[0, 0, 0] / electronvolt - 0.35046350435E+01) < 1e-10
    assert abs(d[0, 1, 0] / electronvolt - 0.213732132354E+01) < 1e-10
    assert abs(d[0, 2, 0] / electronvolt - -.65465465497E+01) < 1e-10
    assert abs(d[0, 2, 1] / electronvolt - -.546876467887E+01) < 1e-10
