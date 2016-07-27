"""
Collection of curve tools
"""

from cmivfx import c, xsi

def addCnsCurve(parent, name, centres, closed=False, degree=1):
    """"Draws a curve through centre points. Curve cv's driven by centre points"""
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


