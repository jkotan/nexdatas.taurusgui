#!/usr/bin/env python
#   This file is part of nexdatas - Tango Server for NeXus data writer
#
#    Copyright (C) 2014-2017 DESY, Jan Kotanski <jkotan@mail.desy.de>
#
#    nexdatas is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    nexdatas is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with nexdatas.  If not, see <http://www.gnu.org/licenses/>.
# 

""" setup.py for setting NeXus MacroGUI """

import os
import sys
from distutils.util import get_platform
from distutils.core import setup
from distutils.command.build import build
from distutils.command.clean import clean
from distutils.command.install_scripts import install_scripts
import shutil

#: package name
TOOL = "nxstaurusgui"
#: package instance
ITOOL = __import__(TOOL)


DATADIR = os.path.join(TOOL, "data")

from sphinx.setup_command import BuildDoc


def read(fname):
    """ read the file 

    :param fname: readme file name
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#: scripts
SCRIPTS = ['nxsmacrogui']

#: package data
package_data = {'nxstaurusgui': ['data/desylogo.png', 'data/config.xml']
                }

release = ITOOL.__version__
version = ".".join(release.split(".")[:2])
name = "NXS Taurus GUI"


#: metadata for distutils
SETUPDATA = dict(
    name="nxstaurusgui",
    version=ITOOL.__version__,
    author="Jan Kotanski",
    author_email="jankotan@gmail.com",
    maintainer="Jan Kotanski",
    maintainer_email="jankotan@gmail.com",
    description=("NXSelector MacroGUI for taurusgui"),
    license=read('COPYRIGHT'),
    keywords="configuration scan nexus sardana recorder tango component data",
    url="https://github.com/jkotan/nexdatas",
    platforms=("Linux"),
    packages=[TOOL, DATADIR],
    scripts=SCRIPTS,
    package_data=package_data,
    cmdclass={'build_sphinx': BuildDoc},
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release)}},
    long_description=read('README.rst')
)


## the main function
def main():
    setup(**SETUPDATA)

if __name__ == '__main__':
    main()
