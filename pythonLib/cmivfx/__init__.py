from win32com.client import Dispatch
from win32com.client import constants as c

# gives us easy access to XSI API
xsi = Dispatch('XSI.Application').Application
xsiMath = Dispatch('XSI.Math')
xsiFactory = Dispatch('XSI.Factory')

"""
Not sure what exactly I'm doing with this class yet, temp header.
"""