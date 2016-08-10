from cmivfx import log
from cmivfx.builder.guide import ComponentGuide
from cmivfx.builder.componentHooks import ComponentHooks

"""
Basic fk ctrl component.
"""

class FkCtrlGuide(ComponentGuide):

    manipulatorNames = ['Root']


class FkCtrl(ComponentHooks):

    def createObjects(self):
        log('Creating objects for Control')
        pass

    def createParameters(self):
        log('Creating Parameters for Control')
        pass

    def createOperators(self):
        log('Creating Operators for Control')
        pass

    def createSlots(self):
        log('Creating Slots for Control')
        pass

    def createConnection(self):
        log('Creating Connection for Control')
        pass