from cmivfx import xsiMath

"""
Helper functions for math in xs
"""

def getDistance(posA, posB):
    """Returns distance between position A and position B"""
    vector = xsiMath.CreateVector3()
    vector.Sub(posB, posA)
    return vector.Length()

# TODO: Dickhead is about to write another function in here because his fkchain is shit. Orientations should
# be set by user in the guide but he wants the aim to be automatic, which just sounds
# like asking for trouble.