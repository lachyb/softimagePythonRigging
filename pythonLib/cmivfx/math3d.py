from cmivfx import xsiMath

"""
Helper functions for math in xsi
"""

def getDistance(posA, posB):
    """Returns distance between position A and position B"""
    vector = xsiMath.CreateVector3()
    vector.Sub(posB, posA)
    return vector.Length()

def getLookAtTransform(position, lookat, normal, axis='xy', negativeScale=False):
    """
    Determines a vector orientation towards lookat parameter, aiming using axis parameter
    :param position: object representing origin of vector
    :param lookat: object to aim towards
    :param normal:
    :param axis: two letter string representing aim and up vectors, eg xy, xz, yz etc
    :param negativeScale: bool. Flips aim and up vectors if true.
    :return: vector aiming towards lookat
    abc arbitrarily represent xyz axis
    """
    a = xsiMath.CreateVector3()
    b = xsiMath.CreateVector3()
    c = xsiMath.CreateVector3()

    a.Sub(lookat, position)
    a.NormalizeInPlace()

    b.Copy(normal)

    if negativeScale:
        a.NegateInPlace()
        b.NegateInPlace()

    c.Cross(a, b)
    c.NormalizeInPlace()

    b.Cross(c, a)
    b.NormalizeInPlace()

    # returns index for given string (e.g. 'y') in string 'xyz'
    aimVector = 'xyz'.index(axis[0])
    upVector = 'xyz'.index(axis[1])

    out = [c] * 3
    out[aimVector] = a
    out[upVector] = b

    rotation = xsiMath.CreateRotation()
    rotation.SetFromXYZAxes(out[0], out[1], out[2])

    transform = xsiMath.CreateTransform()
    transform.SetTranslation(position)
    transform.SetRotation(rotation)
    if negativeScale:
        transform.SetScalingFromValues(-1, -1, -1)

    return transform


# TODO: Dickhead is about to write another function in here because his fkchain is shit. Orientations should
# be set by user in the guide but he wants the aim to be automatic, which just sounds
# like asking for trouble.