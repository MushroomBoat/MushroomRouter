import tkinter as tk
# from tkinter import ttk
from application import Application
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from boat import *


#myboat = Boat('boats\mono\class_40.json', LightSail=True)

#myboat.print_options()
#speed = myboat.get_speed_sail(8.04, 96, myboat.sail_speed[:, :, 0])
#print("actual speed", speed)




# plot = dswind.magnitude.isel(time = 0, step = 0).plot(cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
# ax.barbs(longitude, latitude, dswind.u10.isel(time = 0, step = 0),dswind.u10.isel(time = 0, step = 0), length=3,pivot='middle')




root = tk.Tk()
app = Application(master=root)
app.mainloop()
