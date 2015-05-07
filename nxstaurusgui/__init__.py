#!/usr/bin/env python
#   This file is part of nexdatas - Tango Server for NeXus data writer
#
#    Copyright (C) 2014-2015 DESY, Jan Kotanski <jkotan@mail.desy.de>
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
## \package nxsmacrogui nexdatas
## \file nxselector/__init__.py
# package constructor

""" --- NXS MacroGUI --
GUI for taurusgui
"""

## version of the application
__version__ = "1.0.0"


from config import *
from  . import serverinfo
from  . import config
import xml
import tempfile

def replaceText(node, text):
    if node.firstChild.nodeType == node.TEXT_NODE:
        node.firstChild.replaceWholeText(text)
            

def changeXML():
    with open(config.XML_CONFIG, 'r') as content_file:
        xmlstring = content_file.read()
    print "S1", xmlstring
    indom = None
    if serverinfo.SELECTORSERVER_NAME:
        if not indom:
            indom = xml.dom.minidom.parseString(xmlstring)
        modelnode = indom.getElementsByTagName("model")
        if modelnode:
            replaceText(modelnode[0], serverinfo.SELECTORSERVER_NAME)
            
    if serverinfo.DOOR_NAME:
        if not indom:
            indom = xml.dom.minidom.parseString(xmlstring)
        doornode = indom.getElementsByTagName("DOOR_NAME")
        if doornode:
            replaceText(doornode[0], serverinfo.DOOR_NAME)
    if serverinfo.MACROSERVER_NAME:
        if not indom:
            indom = xml.dom.minidom.parseString(xmlstring)
        macronode = indom.getElementsByTagName("MACROSERVER_NAME")
        if macronode:
            replaceText(macronode[0], serverinfo.DOOR_NAME)
    if indom:
        clxml = indom.toxml()
        f = tempfile.NamedTemporaryFile(delete=False)
        f.write(clxml)
        print clxml
        f.close()
        return f.name

print "MC2", serverinfo.MACROSERVER_NAME
print "DR2", serverinfo.DOOR_NAME
print "SL2", serverinfo.SELECTORSERVER_NAME

#config.XML_CONFIG_DIR = '.'
if __path__:
    config.XML_CONFIG_DIR =  __path__[0]
print "PATH", config.XML_CONFIG_DIR

config.XML_CONFIG = '%s/data/config.xml' % config.XML_CONFIG_DIR
print "CXONF", config.XML_CONFIG
newfile = changeXML()
if newfile:
    print newfile
    config.XML_CONFIG = newfile
print "CONFIG", config.XML_CONFIG



