..
    : IODATA is an input and output module for quantum chemistry.
    :
    : Copyright (C) 2011-2019 The IODATA Development Team
    :
    : This file is part of IODATA.
    :
    : IODATA is free software; you can redistribute it and/or
    : modify it under the terms of the GNU General Public License
    : as published by the Free Software Foundation; either version 3
    : of the License, or (at your option) any later version.
    :
    : IODATA is distributed in the hope that it will be useful,
    : but WITHOUT ANY WARRANTY; without even the implied warranty of
    : MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    : GNU General Public License for more details.
    :
    : You should have received a copy of the GNU General Public License
    : along with this program; if not, see <http://www.gnu.org/licenses/>
    :
    : --


Installation
============

Python 3 (>=3.6) must be installed. Other dependencies will be pulled in with
the instructions below.

IOData can be installed with conda:

.. code-block:: bash

    conda install theochem::iodata

It can also be installed with pip. One of the following is fine, whichever you
prefer:

.. code-block:: bash

    pip install iodata
    pip install iodata --user
    python3 -m pip install iodata
    python3 -m pip install iodata --user


Testing
-------

The tests are automatically run when building with conda, but you may try
them again on your own machine after installation:

.. code-block:: bash

    $ pytest --pyargs iodata
