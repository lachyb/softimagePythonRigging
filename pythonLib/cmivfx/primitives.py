"""
Collection of curve tools
"""

from cmivfx import c, xsi, xsiMath


def addNull(parent, name, tfm=xsiMath.CreateTransform(), size=1, colour=[0, 0, 0],
            primaryIcon=None, shadowIcon=None, shdOffX=None, shdOffY=None, shdOffZ=None,
            shdSclX=None, shdSclY=None, shdSclZ=None):
    """
    Create a null with a given transform, size, color and display
    :param parent: x3dobject, parent object
    :param name: String. Name of the null
    :param tfm: siTransformation. Global transform of the null
    :param size: float.	Display size
    :param colour: list of floats. RGB color (0-1)
    :param primaryIcon: int. Null primary icon
    :param shadowIcon: int. Null shadow icon
    :param shdOffX: float. Null shadow offset position X
    :param shdOffY: float. Null shadow offset position Y
    :param shdOffZ: float. Null shadow offset position Z
    :param shdSclX: float. Null shadow offset scaling X
    :param shdSclY: float. Null shadow offset scaling Y
    :param shdSclZ: float. Null shadow offset scaling Z
    :return null. The newly created null
    """

    null = parent.AddNull(name)
    null.Kinematics.Global.Transform = tfm
    null.size = size

    # Set Null display parameters
    params = {'primary_icon': primaryIcon, 'shadow_icon': shadowIcon, 'shadow_offsetX': shdOffX,
              'shadow_offsetY': shdOffY, 'shadow_offsetZ': shdOffZ, 'shadow_scaleX': shdSclX,
              'shadow_scaleY': shdSclY, 'shadow_scaleZ': shdSclZ}

    keys = params.keys()
    keys.sort()
    for key in keys:
        if params[key] is not None:
            null.ActivePrimitive.Parameters(key).Value = params[key]

    # Set Null Color
    if colour is not None:
        displayProp = null.AddProperty('Display Property')
        displayProp.wirecolorr.Value = colour[0]
        displayProp.wirecolorg.Value = colour[1]
        displayProp.wirecolorb.Value = colour[2]

    return null

def addCnsCurve(parent, name, centres, closed=False, degree=1):
    """Draws a curve through centre points. Curve cv's driven by centre points."""
    centres = list(centres)

    # cubic curves need at least 4 points
    if degree == 3:
        if len(centres) == 2:
            centres.insert(0, centres[0])
            centres.append(centres[-1])
        elif len(centres) == 3:
            centres.append(centres[-1])

    points = []
    for centre in centres:
        x = centre.Kinematics.Global.Transform.PosX
        y = centre.Kinematics.Global.Transform.PosY
        z = centre.Kinematics.Global.Transform.PosZ
        points.extend([x, y, z, 1])

    # draws a curve through given points
    curve = parent.AddNurbsCurve(points, None, closed, degree, c.siNonUniformParameterization, c.siSINurbs, name)

    # add a cluster to given cv [i] on the curve driven by the centre
    for i, centre in enumerate(centres):
        cluster = curve.ActivePrimitive.Geometry.AddCluster(c.siVertexCluster, 'centre{:02d}'.format(i), [i])
        xsi.ApplyOp('ClusterCenter', '{};{}'.format(cluster.FullName, centre.FullName))

    return curve


