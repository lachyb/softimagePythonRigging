from win32com.client import Dispatch
from win32com.client import constants as c
import os

"""
Not sure what exactly I'm doing with this class yet, temp header.
"""

# gives us easy access to XSI API
xsi = Dispatch('XSI.Application').Application
xsiMath = Dispatch('XSI.Math')
xsiFactory = Dispatch('XSI.Factory')

# shorthand for calling LogMessage
log = xsi.LogMessage

def reloadSubModules(path, moduleName):
    for dirPath, subDir, fileNames in os.walk(path):
        for fileName in fileNames:
            if not fileName.endswith('.py'):
                continue

            if fileName == '__init__':
                subModuleName = moduleName
            else:
                subModuleName = moduleName + '.' + fileName[:-3]

            log('reloading {}'.format(subModuleName))

            module = __import__(subModuleName, globals(), locals(), ['*'], -1)
            reload(module)

