import os
import logging
import sys
import platform

import hou
    
import perforce.GlobalVars
from perforce import Utils
from perforce.version import __version__
from perforce.AppInterop.BaseInterop import BaseInterop, BaseCallbacks
from perforce.GUI.Qt import QtCore, QtGui, QtWidgets, __binding__


class HoudiniInterop(BaseInterop):
    @staticmethod
    def setupTestingEnvironment():
        pass

    @staticmethod
    def main_parent_window():
        return hou.ui.mainQtWindow()
  
    @staticmethod
    def getSettingsPath():
        return os.getenv("HOUDINI_USER_PREF_DIR")

    @staticmethod
    def getIconPath():
        return os.path.join(HoudiniInterop.getSettingsPath(), "scripts", "P4Houdini" "perforce", "images")
    
    @staticmethod
    def getSceneFiles():
        return ['.hip', '.hipnc']
    
    @staticmethod
    def getTempPath():
        return os.environ["HOUDINI_TEMP_DIR"]

    @staticmethod
    def getCurrentSceneFile():
        return hou.hipFile.path()


    @staticmethod
    def openScene(filePath):
        hou.hipFile.open(filePath)


    @staticmethod
    def closeWindow(ui):
        pass


    @staticmethod
    def refresh():
        pass


    def initializeMenu(self, entries):
        pass
        # m = nuke.menu( 'Nuke' )
        # self.menu = m.addMenu( 'Perforce' )

    def addMenuDivider(self, label):
        pass
        # self.menu.addSeparator()
       
    def addMenuLabel(self, label):
        pass
        # tmp = self.menu.addCommand(label, lambda: None)
        # tmp.setEnabled(False)

    def addMenuSubmenu(self, label, iconPath, entries):
        pass
        # # Save our current menu
        # parent = self.menu
        # self.menu = parent.addMenu(label, icon=self.sanitizeIconPath(iconPath))

        # # Fill up the submenu
        # self.fillMenu(entries)

        # # Reset our current menu
        # self.menu = parent


    def addMenuCommand(self, label, iconPath, command):
        pass
        # self.menu.addCommand(label, command, icon=self.sanitizeIconPath(iconPath))