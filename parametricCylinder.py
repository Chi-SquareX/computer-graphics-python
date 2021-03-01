from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject


class parametricCylinder(parametricObject):
    """
    These are the inputs to the initializer: cylinder T matrix, cylinder Height, cylinder Radius, cylinder Color, cylinder Reflectance,
    (0.0, 1.0), (0.0, 2.0 * pi), (1.0 / 10.0, pi / 18.0)

    So make some default values for the parameters and the pass it through the super constructor
    """

    def __init__(self, T=matrix(np.identity(4)), cylinder_height=20.0, cylinder_radius=10.0, color=(255, 255, 255),
                 reflectance=(0.2, 0.4, 0.4, 1.0),
                 uRange=(0.0, 1.0), vRange=(0.0, 2*pi), uvDelta=(1.0 / 10.0, pi / 18.0)):
        super().__init__(T, color, reflectance, uRange, vRange, uvDelta)
        self.__cylinder_height = cylinder_height
        self.__cylinder_radius = cylinder_radius

    def getPoint(self, u, v):
        """
        This will give the parametric point given the values of u and v
        :param u: the first parameter value between 0 and 1
        :param v: the second parameter value between 0 and 2*pi
        :return: the 4*1 matrix that represents the parametric form of the cylinder
        """
        P = matrix(np.ones((4, 1)))
        P.set(0, 0, self.__cylinder_radius*sin(v))
        P.set(1, 0, self.__cylinder_radius*cos(v))
        P.set(2, 0, self.__cylinder_height*u)
        return P

    def set_cylinder_height(self, cylinder_height):
        self.__cylinder_height = cylinder_height

    def get_cylinder_height(self):
        return self.__cylinder_height

    def set_cylinder_radius(self, cylinder_radius):
        self.__cylinder_radius = cylinder_radius

    def get_cylinder_radius(self):
        return self.__cylinder_radius
