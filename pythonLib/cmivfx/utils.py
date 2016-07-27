"""
Collection of useful utility scripts
"""

from cmivfx import xsi, c

def searchAndReplace():
    """"Creates a property panel, replaces given phrase for obj in selection"""
    propPanel = xsi.ActiveSceneRoot.AddProperty('CustomProperty', False, 'SearchAndReplace')
    searchParam = propPanel.AddParameter3('Search', c.siString)
    replaceParam = propPanel.AddParameter3('Replace', c.siString)

    panelClosed = xsi.InspectObj(propPanel, '', 'Search and Replace', c.siModal, False)

    searchText = searchParam.Value
    replaceText = replaceParam.Value

    xsi.DeleteObj(propPanel)

    if panelClosed:
        return

    for obj in xsi.Selection:
        obj.Name = obj.Name.replace(searchText, replaceText)
