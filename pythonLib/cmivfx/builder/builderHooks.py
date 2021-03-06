from cmivfx import xsi, log
from datetime import datetime


class BuilderHooks(object):

    """
    Builder takes guide model and creates a 'rig' model from the parameters specified in the guide.
    Rig model contains all rig elements - components, groups, geometry etc.
    Builder needs to be instantiated with instance of guide module.
    """

    def __init__(self, guide):
        self.guide = guide
        self.settings = self.guide.settings
        self.components = {} # dictionary of components to be built

    def build(self):
        """Master call for building rig elements. Logs completion time for convenience."""
        startTime = datetime.now()

        xsi.SetValue('preferences.scripting.cmdlog', False, '')
        self.buildInitialHierarchy()
        self.initComponents()
        self.buildComponents()
        xsi.SetValue('preferences.scripting.cmdlog', True, '')

        endTime = datetime.now()
        log('Build completed in: {}'.format(endTime - startTime))

    def buildInitialHierarchy(self):
        """"Creates default rig model hierarchy for organising rig components."""
        # Rig model (different from guide model)
        self.model = xsi.ActiveSceneRoot.AddModel(None, self.settings['Name'])
        self.model.Properties('Visibility').Parameters('viewvis').Value = False

        # Groups for organisation
        self.hiddenGrp = self.model.AddGroup(None, 'hidden_grp')
        self.unselactableGrp = self.model.AddGroup(None, 'unselactable_grp')
        self.controllersGrp = self.model.AddGroup(None, 'controllers_grp')
        self.deformersGrp = self.model.AddGroup(None, 'deformers_grp')

        self.hiddenGrp.Parameters('viewvis').Value = 0
        self.unselactableGrp.Parameters('selectability').Value = 0
        self.deformersGrp.Parameters('viewvis').Value = 0

        # Nulls for organisation
        self.deformersOrg = self.model.AddNull('deformers_org')
        self.geometryOrg = self.model.AddNull('geometry_org')
        self.hiddenGrp.AddMember(self.deformersOrg)
        self.hiddenGrp.AddMember(self.geometryOrg)

    def initComponents(self):
        """
        For each component collected by the guide, store the component build class in a dictionary.
        """
        for key, guide in self.guide.components.items():
            type_ = guide.type_ # e.g. arm, godnode
            log("init component builder: '{}'. Component type is '{}'".format(key, type_))

            moduleName = type_.lower()
            module = __import__('cmivfx.components.{}'.format(moduleName), globals(), locals(), ['object'], -1)
            ComponentClass = getattr(module, type_) # e.g. cmivfx.components.fkctrl.FkCtrl

            self.components[key] = ComponentClass(self, guide)

    def buildComponents(self):
        """
        Execute each hook for each component in succession - createObjects() for all components,
        then createParameters() for all components etc.
        """
        for i in range(5):
            for key, component in self.components.items():
                component.build[i]()

