from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject


class parametricCircle(parametricObject):

    def __init__(self, T=matrix(np.identity(4)), radius=10.0, color=(255, 255, 255), reflectance=(0.2, 0.4, 0.4, 1.0),
                 uRange=(0.0, 1.0), vRange=(0.0, 2.0 * pi), uvDelta=(1.0 / 10.0, pi / 18.0)):
        super().__init__(T, color, reflectance, uRange, vRange, uvDelta)
        self.__radius = radius

    def getPoint(self, u, v):
        """
        This will give the parametric point given the values of u and v
        :param u: the first parameter value between 0 and 1
        :param v: the second parameter value between 0 and 2*pi
        :return: the 4*1 matrix that represents the parametric form of the circle
        """
        P = matrix(np.ones((4, 1)))
        P.set(0, 0, self.__radius * cos(v) * u)
        P.set(1, 0, self.__radius * sin(v) * u)
        P.set(2, 0, 0.0)
        return P

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius
