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
        log('Creating objects for FkCtrl')
        pass

    def createParameters(self):
        log('Creating Parameters for FkCtrl')
        pass

    def createOperators(self):
        log('Creating Operators for FkCtrl')
        pass

    def createSlots(self):
        log('Creating Slots for FkCtrl')
        pass

    def createConnection(self):
        log('Creating Connection for FkCtrl')
        pass