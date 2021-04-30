import json
from foil import Foil
import numpy as np
from utils import *


class Boat:
    boat_name: object
    hull: float  # polish coefficient
    twa_array = []
    tws_array = []
    sail_name = []
    sail_speed = []
    current_location = object
    destination_location = object

    def __init__(self, **kwargs):
        # Choix des options
        self.Jib_option = True
        self.Spi_option = True
        self.Staysail_option = False
        self.LightJib_option = False
        self.Code0_option = False
        self.HeavyGnk_option = False
        self.LightGnk_option = False
        self.Foil_option = False
        self.Polish_option = False
        self.WinchPro_option = False

        if kwargs.__len__() != 0:
            if 'LightSail' in kwargs:
                if kwargs['LightSail']:
                    self.LightJib_option = True
                    self.LightGnk_option = True

            if 'HeavySail' in kwargs:
                if kwargs['HeavySail']:
                    self.Staysail_option = True
                    self.HeavyGnk_option = True

            if 'Code0' in kwargs:
                if kwargs['Code0']:
                    self.Code0_option = True

            if 'Foil' in kwargs:
                if kwargs['Foil']:
                    self.Foil_option = True

            if 'Polish' in kwargs:
                if kwargs['Polish']:
                    self.Polish_option = True

            if 'WinchPro' in kwargs:
                if kwargs['WinchPro']:
                    self.WinchPro_option = True

            if 'FullPack' in kwargs:
                if kwargs['FullPack']:
                    self.Staysail_option = True
                    self.LightJib_option = True
                    self.Code0_option = True
                    self.HeavyGnk_option = True
                    self.LightGnk_option = True
                    self.Foil_option = True
                    self.Hull_option = True
                    self.WinchPro_option = True
        if self.Foil_option:
            self.foil = Foil()





    def read(self, json_polar_file):
        file = open(json_polar_file, 'r')
        polar_data = json.load(file)
        self.twa_array = np.asarray(polar_data['twa'])
        self.tws_array = np.asarray(polar_data['tws'])
        self.boat_name = (polar_data['label'])
        nb = len(polar_data['sail'])
        self.sail_speed = np.zeros((len(self.twa_array), len(self.tws_array), nb))
        for i in range(nb):
            self.sail_name.append(polar_data['sail'][i]['name'])
            self.sail_speed[:, :, i] = polar_data['sail'][i]['speed']
        # caracteristiques des  foils
        if self.Foil_option:
            self.foil.speedRatio = polar_data['foil']['speedRatio']
            self.foil.twaMin = polar_data['foil']['twaMin']
            self.foil.twaMax = polar_data['foil']['twaMax']
            self.foil.twaMerge = polar_data['foil']['twaMerge']
            self.foil.twsMin = polar_data['foil']['twsMin']
            self.foil.twsMax = polar_data['foil']['twsMax']
            self.foil.twsMerge = polar_data['foil']['twsMerge']

        # polish
        self.hull = polar_data['hull']['speedRatio']

    def get_speed_sail(self, tws, twa, sail_polar):
        return interp2d_linear(twa, tws, self.twa_array, self.tws_array, sail_polar)
