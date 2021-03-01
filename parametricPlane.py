from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject


class parametricPlane(parametricObject):
    """
    These are the inputs to the initializer:
    planeT, planeWidth, planeLength, planeCol, planeRef, (0.0, 1.0), (0.0, 1.0), (1.0 / 10.0, 1.0 / 10.0)

    So make some default values for the parameters and the pass it through the super constructor

    The plane width is the width of plane
    The plane_length is the length of the plane
    """

    def __init__(self, T=matrix(np.identity(4)), plane_width=20.0, plane_length=20.0, color=(255, 255, 255),
                 reflectance=(0.2, 0.4, 0.4, 1.0),
                 uRange=(0.0, 1.0), vRange=(0.0, 1.0), uvDelta=(1.0 / 10.0, 1.0 / 10.0)):

        super().__init__(T, color, reflectance, uRange, vRange, uvDelta)
        self.__plane_width = plane_width
        self.__plane_length = plane_length

    def getPoint(self, u, v):
        """
        This will give the parametric point given the values of u and v
        :param u: the first parameter value between 0 and 1
        :param v: the second parameter value between 0 and 1
        :return: the 4*1 matrix that represents the parametric form of the plane
        """
        P = matrix(np.ones((4, 1)))
        P.set(0, 0, u*self.__plane_width)
        P.set(1, 0, v*self.__plane_length)
        P.set(2, 0, 0)
        return P

    def set_plane_width(self, plane_width):
        self.__plane_width = plane_width

    def get_plane_width(self):
        return self.__plane_width

    def set_plane_length(self, plane_length):
        self.__plane_length = plane_length

    def get_plane_length(self):
        return self.__plane_length