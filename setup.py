#!/usr/bin/env python
#   This file is part of nexdatas - Tango Server for NeXus data writer
#
#    Copyright (C) 2014-2016 DESY, Jan Kotanski <jkotan@mail.desy.de>
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
## \package nxstaurusgui nexdatas
## \file setup.py
# GUI for setting NeXus Sardana Recorder

""" setup.py for NXS Component Designer """

import os
import sys
from distutils.util import get_platform
from distutils.core import setup
from distutils.command.build import build
from distutils.command.clean import clean
from distutils.command.install_scripts import install_scripts
import shutil

## package name
TOOL = "nxstaurusgui"
## package instance
ITOOL = __import__(TOOL)


DATADIR = os.path.join(TOOL, "data")

## reading a file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

SCRIPTS = ['nxsmacrogui']


package_data = {'nxstaurusgui': ['data/desylogo.png', 'data/config.xml']
                }


## metadata for distutils
SETUPDATA = dict(
    name="nxstaurusgui",
    version=ITOOL.__version__,
    author="Jan Kotanski",
    author_email="jankotan@gmail.com",
    maintainer="Jan Kotanski",
    maintainer_email="jankotan@gmail.com",
    description=("NXSelector MacroGUI for taurusgui"),
    license=read('COPYRIGHT'),
#    license="GNU GENERAL PUBLIC LICENSE, version 3",
    keywords="configuration scan nexus sardana recorder tango component data",
    url="https://github.com/jkotan/nexdatas",
    platforms=("Linux", " Windows", " MacOS "),
    packages=[TOOL, DATADIR],
    scripts=SCRIPTS,
    package_data=package_data,
    long_description=read('README'),
)


## the main function
def main():
    setup(**SETUPDATA)

if __name__ == '__main__':
    main()
