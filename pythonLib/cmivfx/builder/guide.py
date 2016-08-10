from cmivfx import log, c

"""
Guide module. Currently very basic - checks your guide model has the appropriate components,
and initialises default name and colour parameters.
"""

class Guide(object):

    def __init__(self, model):
        self.model = model
        self.settings = {'Name': 'unknown',
                         'colour_R': '0, 0, 1',
                         'colour_M': ',75, .25, .75',
                         'colour_L': '1, 0, 0'}

        # dict of components guide found in the scene model
        self.components = {}

        # We instantiate these once we know if the model is valid
        self.settingsProperty = None
        self.componentsOrg = None

        assert self.isValid(self.model), 'Guide is invalid'
        self.initFromModel()

    def isValid(self, model):
        """Check that required elements of model exist."""
        if not model.Type == '#model':
            log('Guide is not of type "model"', c.siError)
            return False

        self.settingsProperty = self.model.Properties('Settings')
        if not self.settingsProperty:
            log('Guide missing "Settings" property', c.siError)
            return False

        self.componentsOrg = self.model.FindChild('component_org')
        if not self.componentsOrg:
            log('Guide missing "component_org" null', c.siError)
            return False

        return True

    def initFromModel(self):
        """
        Stores values specified by user in model into self.settings.
        Stores all specified component properties into dictionary as components.
        """
        for param in self.settingsProperty.Parameters:
            self.settings[param.ScriptName] = param.Value

        self.settings['colour_R'] = [float(s) for s in self.settings['colour_R'].split(', ')]
        self.settings['colour_M'] = [float(s) for s in self.settings['colour_M'].split(', ')]
        self.settings['colour_L'] = [float(s) for s in self.settings['colour_L'].split(', ')]

        # For each property (custom param set) underneath the componentsOrg null, store the values given
        # in the property as a component - adding it to the components dictionary
        for property_ in self.componentsOrg.Properties:
            if not property_.Name.startswith('settings'):
                continue

            type_ = property_.Parameters('Type_').Value # component type, i.e. arm, godnode
            name = property_.Parameters('Name_').Value # arbitrary name of component
            location = property_.Parameters('Location').Value # L, R, M

            log("init component guide: '{}_{}'. Component type is '{}'".format(name, location, type_))

            moduleName = type_.lower()
            module = __import__('cmivfx.components.{}'.format(moduleName), globals(), locals(), ['object'], -1)
            GuideClass = getattr(module, '{}Guide'.format(type_))

            # setting value in dict of component name + location to be instance of component GuideClass
            self.components['{}_{}'.format(name, location)] = GuideClass(property_)


class ComponentGuide(object):
    """
    Parent Class for all component guides.
    Initialises component properties.
    """
    # global variable for storing name of component. Overriden by child classes.
    manipulatorNames = []

    def __init__(self, property_):
        self.property = property_
        self.model = self.property.model

        self.type_ = self.property.Parameters('Type_').Value
        self.name = self.property.Parameters('Name_').Value
        self.location = self.property.Parameters('Location').Value

        # store each param's scriptName and Value as key/value pairs
        self.settings = {}
        for param in self.property.Parameters:
            self.settings[param.ScriptName] = param.Value

        self.pos = {}
        self.tfm = {}
        self.apos = []
        self.atfm = []

        for manipulatorName in self.manipulatorNames:
            manipulator = self.model.FindChild(self.getManipulatorName(manipulatorName))
            assert manipulator, 'Missing manipulator: {}'.format(self.getManipulatorName(manipulatorName))
            self.saveManipulatorTransform(manipulator, manipulatorName)

    def saveManipulatorTransform(self, manipulator, manipulatorName):
        tfm = manipulator.Kinematics.Global.Transform
        tfm.SetScalingFromValues(1, 1, 1)

        self.pos[manipulatorName] = tfm.Translation
        self.tfm[manipulatorName] = tfm
        self.apos.append(tfm.Translation)
        self.atfm.append(tfm)

    def getManipulatorName(self, name):
        """"Helper method to return full name of manipulator in scene."""
        return 'Gde_{}_{}_{}'.format(self.name, self.location, name)

