from cmivfx import primitives 

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

        # TODO: keep refactorying dickheads missing code, why couldn't this be included in tutorial...
        ctrl = primitives.addNull(parent, self.getName(name + "_ctl"), tfm, size, colour, primaryIcon,
                                  shadowIcon, shdOffX, shdOffY, shdOffZ, shdSclX, shdSclY, shdSclZ)
        self.controllersGrp.AddMember(ctrl)
        return ctrl