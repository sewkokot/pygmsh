# -*- coding: utf-8 -*-
#
from .point_base import PointBase


class Point(PointBase):
    """
    Creates an elementary point.

    x : array-like[3]
        Give the three X, Y and Z coordinates of the
        point in the three-dimensional Euclidean space.
    lcar : float
        The prescribed mesh element size at this point.
    """

    def __init__(self, x, lcar=None):
        super(Point, self).__init__()

        self.x = x
        self.lcar = lcar

        # Points are always 3D in gmsh
        if lcar is not None:
            self.code = "\n".join(
                [
                    "{} = newp;".format(self.id),
                    "Point({}) = {{{!r}, {!r}, {!r}, {!r}}};".format(
                        self.id, x[0], x[1], x[2], lcar
                    ),
                ]
            )
        else:
            self.code = "\n".join(
                [
                    "{} = newp;".format(self.id),
                    "Point({}) = {{{!r}, {!r}, {!r}}};".format(
                        self.id, x[0], x[1], x[2]
                    ),
                ]
            )
        return
