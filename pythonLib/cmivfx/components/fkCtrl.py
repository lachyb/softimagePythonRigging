from cmivfx import siLog
from cmivfx.builder.guide import ComponentGuide
from cmivfx.builder.componentHooks import ComponentHooks

"""
Basic fk ctrl component.
"""

class FkCtrlGuide(ComponentGuide):

    manipulatorNames = ['Root']


class FkCtrl(ComponentHooks):

    def createObjects(self):
        siLog.info('Creating objects for FkCtrl')
        pass

    def createParameters(self):
        siLog.info('Creating Parameters for FkCtrl')
        pass

    def createOperators(self):
        siLog.info('Creating Operators for FkCtrl')
        pass

    def createSlots(self):
        siLog.info('Creating Slots for FkCtrl')
        pass

    def createConnection(self):
        siLog.info('Creating Connections for FkCtrl')
        pass