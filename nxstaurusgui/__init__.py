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


from  . import serverinfo
from  . import config
from xml.dom import minidom
import tempfile
import PyTango


def replaceText(node, text):
    if node.firstChild.nodeType == node.TEXT_NODE:
        node.firstChild.replaceWholeText(text)

def findDevices():
    db = PyTango.Database()
    if not serverinfo.SELECTORSERVER_NAME:
        dvs = db.get_device_exported_for_class("NXSRecSelector")

        for dv in dvs:
            try:
                dp = PyTango.DeviceProxy(dv)
                dp.ping()
                if not serverinfo.DOOR_NAME:
                    serverinfo.DOOR_NAME = dp.Door
                serverinfo.SELECTORSERVER_NAME = dv
                break
            except:
                pass
    elif not serverinfo.DOOR_NAME:
        try:
            dp = PyTango.DeviceProxy(serverinfo.SELECTORSERVER_NAME)
            dp.ping()
            serverinfo.DOOR_NAME = dp.Door
        except:
            pass
    
    if not serverinfo.SELECTORSERVER_NAME:
        serverinfo.SELECTORSERVER_NAME ='module'
    elif not serverinfo.MACROSERVER_NAME:
        dvs = db.get_device_exported_for_class("MacroServer")
        for dv in dvs:
            try:
                dp = PyTango.DeviceProxy(dv)
                dp.ping()
                dl = dp.DoorList
                if serverinfo.DOOR_NAME in dl:
                    serverinfo.MACROSERVER_NAME = dv
                    break
            except:
                pass


        

def changeXML(ifile):
    with open(ifile, 'r') as content_file:
        xmlstring = content_file.read()
    indom = None
    findDevices()
    if serverinfo.SELECTORSERVER_NAME:
        if not indom:    
            indom = minidom.parseString(xmlstring)
        modelnode = indom.getElementsByTagName("model")
        if modelnode:
            replaceText(modelnode[0], serverinfo.SELECTORSERVER_NAME)
    if serverinfo.DOOR_NAME:
        if not indom:    
            indom = minidom.parseString(xmlstring)
        doornode = indom.getElementsByTagName("DOOR_NAME")
        if doornode:
            replaceText(doornode[0], serverinfo.DOOR_NAME)
    if serverinfo.MACROSERVER_NAME:
        if not indom:    
            indom = minidom.parseString(xmlstring)
        macronode = indom.getElementsByTagName("MACROSERVER_NAME")
        if macronode:
            replaceText(macronode[0], serverinfo.MACROSERVER_NAME)
    if indom:        
        clxml = indom.toxml()
        if serverinfo.TMPFILE:
            f = open(serverinfo.TMPFILE, 'w')    
        else:
            f = tempfile.NamedTemporaryFile(delete=False)
        f.write(clxml)
#        print "TEMPORARY", clxml
        f.close()
        serverinfo.TMPFILE = f.name
        return f.name

if serverinfo.FIND:
    newfile = changeXML('%s/data/config.xml' % __path__[0])
    if newfile:
        config.XML_CONFIG = newfile

from config import *


