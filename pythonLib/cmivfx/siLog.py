"""
Simple wrapper for native softimage logging system.
"""

from win32com.client import Dispatch
from win32com.client import constants as c

xsi = Dispatch('XSI.Application').Application # gives us easy access to XSI API

# TODO: I'm guessing there might be a better way to do this using a class and not having to repeat
# the 'message' param throughout?
def fatal(message):
    xsi.LogMessage(message, c.fatal)

def warning(message):
    xsi.LogMessage(message, c.siWarning)

def info(message):
    xsi.LogMessage(message, c.siInfo)

def error(message):
    xsi.LogMessage(message, c.siError)

def debug(message):
    xsi.LogMessage(message, c.siVerbose)