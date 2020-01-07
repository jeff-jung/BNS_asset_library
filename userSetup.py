from pymel import mayautils
import maya.cmds as cmds

def dyshelf_loader():
    shelf_plugins = "dynamicShelf"
    cmds.loadPlugin( shelf_plugins)

if not cmds.about(batch=True):
    mayautils.executeDeferred(dyshelf_loader())