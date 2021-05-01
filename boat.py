import json
from foil import Foil
import numpy as np
from utils import *
import xarray as xr


class Boat:
    sail_name = []
    # sail_speed = []
    current_location = object
    destination_location = object

    def __init__(self, json_boat_file, **kwargs):
        # Choix des options
        self.twa_array = []
        self.tws_array = []
        self.hull = 1
        self.boat_name = "none"
        self.Jib_option = True
        self.Spi_option = True
        self.sail_speed = []
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
        self.read(json_boat_file)

    def read(self, json_polar_file):
        file = open(json_polar_file, 'r')
        polar_data = json.load(file)
        self.twa_array = np.asarray(polar_data['twa'])
        self.tws_array = np.asarray(polar_data['tws'])
        self.boat_name = (polar_data['label'])
        nb_possible_sail = len(polar_data['sail'])
        nb_selected_sail = self.get_nb_selected_sail()
        #print('nb de voile sélectionné:', nb_selected_sail)
        self.sail_speed = np.zeros((len(self.twa_array), len(self.tws_array), nb_selected_sail))
        index = 0
        if self.Jib_option:
            self.sail_name.append(polar_data['sail'][0]['name'])
            self.sail_speed[:, :, index] = polar_data['sail'][0]['speed']
            index = index + 1
        if self.Spi_option:
            self.sail_name.append(polar_data['sail'][1]['name'])
            self.sail_speed[:, :, index] = polar_data['sail'][1]['speed']
            index = index + 1
        if self.Staysail_option:
            self.sail_name.append(polar_data['sail'][2]['name'])
            self.sail_speed[:, :, index] = polar_data['sail'][2]['speed']
            index = index + 1
        if self.LightJib_option:
            self.sail_name.append(polar_data['sail'][3]['name'])
            self.sail_speed[:, :, index] = polar_data['sail'][3]['speed']
            index = index + 1
        if self.Code0_option:
            self.sail_name.append(polar_data['sail'][4]['name'])
            self.sail_speed[:, :, index] = polar_data['sail'][4]['speed']
            index = index + 1
        if self.HeavyGnk_option:
            self.sail_name.append(polar_data['sail'][5]['name'])
            self.sail_speed[:, :, index] = polar_data['sail'][5]['speed']
            index = index + 1
        if self.LightGnk_option:
            self.sail_name.append(polar_data['sail'][6]['name'])
            self.sail_speed[:, :, index] = polar_data['sail'][6]['speed']
            index = index + 1
        #print(self.sail_name)
        #print(self.sail_speed)

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

    def print_options(self):
        print("Jib:", self.Jib_option)
        print("Spi:", self.Spi_option)
        print("LightJib:", self.LightJib_option)
        print("LightGnk", self.LightGnk_option)
        print("Staysail:", self.Staysail_option)
        print("HeavyGnk:", self.HeavyGnk_option)
        print("Code0:", self.Code0_option)
        print("Foil:", self.Foil_option)
        print("Polish:", self.Polish_option)
        print("WinchPro:", self.WinchPro_option)

    def get_nb_selected_sail(self):
        nb = 0
        if self.Jib_option:
            nb = nb + 1
        if self.Spi_option:
            nb = nb + 1
        if self.Staysail_option:
            nb = nb + 1
        if self.LightJib_option:
            nb = nb + 1
        if self.Code0_option:
            nb = nb + 1
        if self.HeavyGnk_option:
            nb = nb + 1
        if self.LightGnk_option:
            nb = nb + 1
        return nb
