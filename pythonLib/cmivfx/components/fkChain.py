from cmivfx import siLog
from cmivfx.builder.guide import ComponentGuide
from cmivfx.builder.componentHooks import ComponentHooks

"""
Creates a chain of fk controls of arbitrary length
"""

class FkChainGuide(ComponentGuide):

    manipulatorNames = ['#',]


class FkChain(ComponentHooks):

    def createObjects(self):
        siLog.info('Creating objects for FkChain')

        parent = self.model
        for i, position in enumerate(self.guide.apos[:-1]):
            nextPostion = self.guide.apos[i + 1]
            ctrl = self.addCtrl(parent, str(i), self.guide.atfm[i], primaryIcon=0, shadowIcon=4,
                                shdSclX=1, shdSclY=.25, shdSclZ=.25, shdOffX=.5)
            parent = ctrl

    def createParameters(self):
        siLog.info('Creating Parameters for FkChain')
        pass

    def createOperators(self):
        siLog.info('Creating Operators for FkChain')
        pass

    def createSlots(self):
        siLog.info('Creating Slots for FkChain')
        pass

    def createConnection(self):
        siLog.info('Creating Connection for FkChain')
        pass