from cmivfx import log, c

"""
Guide module. Currently very basic - checks your guide model has the appropriate components,
and initialises default name and colour parameters.
"""

class Guide(object):

    def __init__(self, model):
        self.model = model
        self.settings = {'Name': 'unknown',
                         'colour_R': '0, 0, 1', 'colour_M': ',75, .25, .75', 'colour_L': '1, 0, 0'}

        # we instantiate these once we know if the model is valid
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
        """"Store values specified by user in model into self.settings"""
        for param in self.settingsProperty.Parameters:
            self.settings[param.ScriptName] = param.Value

        self.settings['colour_R'] = [float(s) for s in self.settings['colour_R'].split(', ')]
        self.settings['colour_M'] = [float(s) for s in self.settings['colour_M'].split(', ')]
        self.settings['colour_L'] = [float(s) for s in self.settings['colour_L'].split(', ')]
