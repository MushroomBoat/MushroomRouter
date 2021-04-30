class Options:

    def __init__(self, **kwargs):
        self.Jib = True
        self.Spi = True
        self.Staysail = False
        self.LightJib = False
        self.Code0 = False
        self.HeavyGnk = False
        self.LightGnk = False
        self.Foil = False
        self.Polish = False
        self.WinchPro = False

        if kwargs.__len__() != 0:
            if 'LightSail' in kwargs:
                if kwargs['LightSail']:
                    self.LightJib = True
                    self.LightGnk = True

            if 'HeavySail' in kwargs:
                if kwargs['HeavySail']:
                    self.Staysail = True
                    self.HeavyGnk = True

            if 'Code0' in kwargs:
                if kwargs['Code0']:
                    self.Code0 = True

            if 'Foil' in kwargs:
                if kwargs['Foil']:
                    self.Foil = True

            if 'Polish' in kwargs:
                if kwargs['Polish']:
                    self.Polish = True

            if 'WinchPro' in kwargs:
                if kwargs['WinchPro']:
                    self.WinchPro = True

            if 'FullPack' in kwargs:
                if kwargs['FullPack']:
                    self.Staysail = True
                    self.LightJib = True
                    self.Code0 = True
                    self.HeavyGnk = True
                    self.LightGnk = True
                    self.Foil = True
                    self.Hull = True
                    self.WinchPro = True

    def print_options(self):
        print("Jib", self.Jib)
        print("Spi", self.Spi)
        print("LightJib", self.LightJib)
        print("LightGnk", self.LightGnk)
        print("Staysail", self.Staysail)
        print("HeavyGnk", self.HeavyGnk)
        print("Code0", self.Code0)
        print("Foil", self.Foil)
        print("Polish", self.Polish)
        print("WinchPro", self.WinchPro)





