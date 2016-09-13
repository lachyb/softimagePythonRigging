from cmivfx import siLog, xsiMath, xsi
from cmivfx.builder.guide import ComponentGuide
from cmivfx.builder.componentHooks import ComponentHooks
from cmivfx import math3d

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
            distance = math3d.getDistance(position, nextPostion)

            normal = xsiMath.CreateVector3(0, 0, 1)
            normal.MulByRotationInPlace(self.guide.atfm[i].Rotation)
            transform = math3d.getLookAtTransform(position, nextPostion, normal, axis='xz', negativeScale=self.negative)

            ctrl = self.addCtrl(parent, str(i), transform, primaryIcon=0, shadowIcon=4,
                                shdSclX=distance, shdSclY=.25, shdSclZ=.25, shdOffX=distance*.5)
            xsi.SetNeutralPose(ctrl)
            self.addDeformer(ctrl, str(i))

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
        siLog.info('Creating Connections for FkChain')
        pass