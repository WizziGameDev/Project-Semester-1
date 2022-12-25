import numpy as np
import os

os.system('cls')
# radian.. dan sudut.. menjadi attribut dari object (s)
class sudut_trigono:  # Class

    def data_sin(self, data):  # Function
        ''' sin '''
        self.radianSin = np.sin(data)
        self.sudutSin = np.sin(np.deg2rad(data))
        print(' ===== SIN =====')
        print(f" Radian\t: {self.radianSin:.3f}")
        print(f" Sudut\t: {self.sudutSin:.2f}\n")

    def data_cos(self, data):
        ''' cos '''
        self.radianCos = np.cos(data)
        self.sudutCos = np.cos(np.deg2rad(data))
        print(' ===== COS =====')
        print(f" Radian\t: {self.radianCos:.3f}")
        print(f" Sudut\t: {self.sudutCos:.2f}\n")

    def data_tan(self, data):
        ''' tan '''
        self.radianTan = np.tan(data)
        self.sudutTan = np.tan(np.deg2rad(data))
        print(' ===== TAN =====')
        print(f" Radian\t: {self.radianTan:.3f}")
        print(f" Sudut\t: {self.sudutTan:.2f}")


s = sudut_trigono()  # Object (s) dengan class sudut_trigonometri
s.data_sin(60)
s.data_cos(60)
s.data_tan(45)
