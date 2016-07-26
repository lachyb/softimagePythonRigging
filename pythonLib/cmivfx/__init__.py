"""
Initialises core components of XSI API, and provides capability to reload all modules
in the project directory.
"""

from win32com.client import Dispatch
from win32com.client import constants as c
import os

# gives us easy access to XSI API
xsi = Dispatch('XSI.Application').Application
xsiMath = Dispatch('XSI.Math')
xsiFactory = Dispatch('XSI.Factory')

# shorthand for calling LogMessage
log = xsi.LogMessage

def _reload():
    reloadSubModules(__path__[0], 'cmivfx')

def reloadSubModules(path, moduleName):
    """
    Reloads all modules in given path.
    :param path: primary directory path to modules, i.e. Documents/PythonPrj/exampleModule
    :param moduleName: name of the top module. This param could be removed by storing
    string contents before last '/'.
    """
    # TODO: Currently reloads all modules, should only reload those with changes.
    for dirPath, dirNames, fileNames in os.walk(path):
        for fileName in fileNames:
            if not fileName.endswith('.py'):
                continue

            if fileName == '__init__':
                subModuleName = moduleName
            else:
                subModuleName = moduleName + '.' + fileName[:-3] # eg cmivfx.subModule

            log('reloading {}'.format(subModuleName))
            try:
                module = __import__(subModuleName, globals(), locals(), ['*'], -1)
                reload(module)

            except ImportError as e:
                for arg in e.args:
                    log(arg, c.siError)

            except Exception as e:
                for arg in e.args:
                    log(arg, c.siError)

        for dirName in dirNames:
            reloadSubModules(path='{p}\{dn}'.format(p=path, dn=dirName),
                             moduleName='{mn}.{dn}'.format(mn=moduleName, dn=dirName))
        # we need to break here otherwise we reload cmivfx.__init__ again... not sure why??
        break



