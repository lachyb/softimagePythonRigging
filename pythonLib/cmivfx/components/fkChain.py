from cmivfx import log
from cmivfx.builder.guide import ComponentGuide
from cmivfx.builder.componentHooks import ComponentHooks

"""
Creates a chain of fk controls of arbitrary length
"""

class FkChainGuide(ComponentGuide):

    manipulatorNames = ['#']


class FkChain(ComponentHooks):

    def createObjects(self):
        log('Creating objects for FkChain')
        pass

    def createParameters(self):
        log('Creating Parameters for FkChain')
        pass

    def createOperators(self):
        log('Creating Operators for FkChain')
        pass

    def createSlots(self):
        log('Creating Slots for FkChain')
        pass

    def createConnection(self):
        log('Creating Connection for FkChain')
        pass