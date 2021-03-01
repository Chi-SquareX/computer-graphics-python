import operator
from math import *
import numpy as np
from matrix import matrix


class cameraMatrix:

    def __init__(self, window, UP, E, G, nearPlane=10.0, farPlane=50.0, theta=90.0):
        self.__UP = UP.normalize()
        self.__E = E
        self.__G = G
        self.__np = nearPlane
        self.__fp = farPlane
        self.__width = window.getWidth()
        self.__height = window.getHeight()
        self.__theta = theta
        self.__aspect = self.__width / self.__height
        self.__npHeight = self.__np * (pi / 180.0 * self.__theta / 2.0)
        self.__npWidth = self.__npHeight * self.__aspect

        Mp = self.__setMp(self.__np, farPlane)
        T1 = self.__setT1(self.__np, self.__theta, self.__aspect)
        S1 = self.__setS1(self.__np, self.__theta, self.__aspect)
        T2 = self.__setT2()
        S2 = self.__setS2(self.__width, self.__height)
        W2 = self.__setW2(self.__height)

        self.__N = (self.__E - self.__G).removeRow(3).normalize()
        self.__U = self.__UP.removeRow(3).crossProduct(self.__N).normalize()
        self.__V = self.__N.crossProduct(self.__U)

        self.__Mv = self.__setMv(self.__U, self.__V, self.__N, self.__E)
        self.__C = W2 * S2 * T2 * S1 * T1 * Mp
        self.__M = self.__C * self.__Mv

    def __setMv(self, U, V, N, E):
        return matrix(np.array([[U.get(0, 0), U.get(1, 0), U.get(2, 0),
                                 -U.get(0, 0) * E.get(0, 0) - U.get(1, 0) * E.get(1, 0) - U.get(2, 0) * E.get(2, 0)],
                                [V.get(0, 0), V.get(1, 0), V.get(2, 0),
                                 -V.get(0, 0) * E.get(0, 0) - V.get(1, 0) * E.get(1, 0) - V.get(2, 0) * E.get(2, 0)],
                                [N.get(0, 0), N.get(1, 0), N.get(2, 0),
                                 -N.get(0, 0) * E.get(0, 0) - N.get(1, 0) * E.get(1, 0) - N.get(2, 0) * E.get(2, 0)],
                                [0, 0, 0, 1]]))

    def __setMp(self, nearPlane, farPlane):
        a = -(farPlane + nearPlane) / (farPlane - nearPlane)
        b = -2 * farPlane * nearPlane / (farPlane - nearPlane)
        return matrix(np.array([[nearPlane, 0, 0, 0],
                                [0, nearPlane, 0, 0],
                                [0, 0, a, b],
                                [0, 0, -1, 0]]))

    def __setT1(self, nearPlane, theta, aspect):
        t = nearPlane * np.tan((np.pi / 180) * (theta / 2))
        b = -t
        r = aspect * t
        l = -r
        return matrix(np.array([[1, 0, 0, -(r + l) / 2],
                                [0, 1, 0, -(t + b) / 2],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]]))

    def __setS1(self, nearPlane, theta, aspect):
        t = nearPlane * np.tan(np.pi / 180 * theta / 2)
        b = -t
        r = aspect * t
        l = -r
        return matrix(np.array([[-2 / (r - l), 0, 0, 0],
                                [0, -2 / (t - b), 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]]))

    def __setT2(self):
        return matrix(np.array([[1, 0, 0, 1],
                                [0, 1, 0, 1],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]]))

    def __setS2(self, width, height):
        return matrix(np.array([[width / 2, 0, 0, 0],
                                [0, height / 2, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]]))

    def __setW2(self, height):
        return matrix(np.array([[1, 0, 0, 0],
                                [0, -1, 0, height],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]]))

    def worldToViewingCoordinates(self, P):
        return self.__Mv * P

    def worldToImageCoordinates(self, P):
        return self.__M * P

    def worldToPixelCoordinates(self, P):
        return self.__M * P.scalarMultiply(1.0 / (self.__M * P).get(3, 0))

    def viewingToImageCoordinates(self, P):
        return self.__C * P

    def viewingToPixelCoordinates(self, P):
        return self.__C * P.scalarMultiply(1.0 / (self.__C * P).get(3, 0))

    def imageToPixelCoordinates(self, P):
        return P.scalarMultiply(1.0 / P.get(3, 0))

    def getUP(self):
        return self.__UP

    def getU(self):
        return self.__U

    def getV(self):
        return self.__V

    def getN(self):
        return self.__N

    def getE(self):
        return self.__E

    def getG(self):
        return self.__G

    def getMv(self):
        return self.__Mv

    def getC(self):
        return self.__C

    def getM(self):
        return self.__M

    def getNp(self):
        return self.__np

    def getFp(self):
        return self.__fp

    def getTheta(self):
        return self.__theta

    def getAspect(self):
        return self.__aspect

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getNpHeight(self):
        return self.__npHeight

    def getNpWidth(self):
        return self.__npWidth
