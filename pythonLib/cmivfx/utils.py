"""
Collection of useful utility scripts
"""

from cmivfx import xsi, c

def searchAndReplace():
    prop = xsi.ActiveSceneRoot.AddProperty(Preset='CustomProperty', BranchFlag=False, Name='SearchAndReplace')
