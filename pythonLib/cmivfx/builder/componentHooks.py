from cmivfx import primitives, xsiMath

class ComponentHooks(object):
    """
    Component Control Hooks. Base class for all components. Outlines build
    sequence for components, grabbing required data first from the guide inside __init__
    """
    def __init__(self, builder, guide):

        self.builder = builder
        self.guide = guide
        self.settings = self.guide.settings
        self.model = self.builder.model

        self.hiddenGrp = self.builder.hiddenGrp
        self.unselectableGrp = self.builder.unselactableGrp
        self.controllersGrp = self.builder.controllersGrp
        self.deformersGrp = self.builder.deformersGrp

        self.deformersOrg = self.builder.deformersOrg

        self.name = self.guide.name
        self.location = self.guide.location
        self.negative = self.location == 'R'

        # the five stages of a components build process. Like rigHooks I guess, createsObjects
        # for ALL components, then createsParameters for ALL components etc etc
        self.build = [self.createObjects, self.createParameters, self.createOperators,
                      self.createSlots, self.createConnection]

    def createObjects(self):
        pass

    def createParameters(self):
        pass

    def createOperators(self):
        pass

    def createSlots(self):
        pass

    def createConnection(self):
        pass

    # TODO: definitely feel like this shit should be in a different class, seperated from the hooks
    # TODO: would be clearer to use a dict for primary/shadow icon so shape names could be entered instead
    # of random numbers. e.g. just type 'circleArrows' instead of 5 or whatever.
    def addCtrl(self, parent, name, tfm, size=1, colour=None, primaryIcon=None, shadowIcon=None,
                shdOffX=None, shdOffY=None, shdOffZ=None, shdSclX=None, shdSclY=None, shdSclZ=None):
        """
        Creates a controller.
        :param parent. si3dobject. Parent object
        :param name. String. Local name of the controller
        :param tfm. siTransformation. Global transform of the controller
        :param size. Float. Display size
        :param colour. List of float. RGB color (0-1)
        :param primaryIcon. int. Null primary icon
        :param shadowIcon int. Null shadow icon
        :param shdOffX float. Null shadow offset position X
        :param shdOffY float. Null shadow offset position Y
        :param shdOffZ float. Null shadow offset position Z
        :param shdSclX float. Null shadow offset scaling X
        :param shdSclY float. Null shadow offset scaling Y
        :param shdSclZ float. Null shadow offset scaling Z
        :return	The newly created null
        """
        ctrl = primitives.addNull(parent, self.getName(name + '_ctl'), tfm, size, colour, primaryIcon,
                                  shadowIcon, shdOffX, shdOffY, shdOffZ, shdSclX, shdSclY, shdSclZ)
        self.controllersGrp.AddMember(ctrl)
        return ctrl

    # def addNull(self, parent, name, tfm=xsiMath.CreateTransform()):
    #     """
    #     Creates a null
    #     :param parent. si3dobject. parent object
    #     :param name. string. Local name of the controller
    #     :param tfm. siTransformation. Global transform of the null
    #     :return	null. The newly created null
    #     """
    #     null = primitives.addNull(parent, self.getName(name), tfm)
    #     self.hiddenGrp.AddMember(null)
    #
    #     return null

    def getName(self, name):
        """Returns the fullname of an object to make sure each object has a unique name."""
        # NOTE: self.name is the name of the object in the guide
        return '{guideName}_{l}_{objName}'.format(guideName=self.name, l=self.location, objName=name)

    def addDeformer(self, parent, localName):
        transform = parent.Kinematics.Global.Transform
        deformer = primitives.addNull(self.deformersOrg, self.getName('{}_dfmr'.format(localName)),
                                      transform, colour=[0, 1, 0], size=.25, primaryIcon=4, visible=False)
        deformer.Kinematics.AddConstraint('Pose', parent, False)
        self.deformersGrp.AddMember(deformer)
        return deformer
