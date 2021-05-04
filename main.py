import tkinter as tk
# from tkinter import ttk
from application import Application
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from boat import *







#myboat = Boat('boats\mono\class_40.json', LightSail=True)

# myboat.print_options()
#speed = myboat.get_speed_sail(8.04, 96, myboat.sail_speed[:, :, 0])
#print("actual speed", speed)


# myboat.plotpolar(0)


def get_zezo_grib():
    import wget
    import os
    if os.path.exists('all.grib'):
        os.remove('all.grib')
    urlzezo = "http://zezo.org/grib/gribv1/all.grib"
    result = wget.download(urlzezo, 'all.grib')
    print("Grib téléchargé")
    return result


"""def submit_polar():
    if (float(sv.get()) >= 0) and (float(sv.get()) <= 40):
        print('svget', sv.get())
        #ax.plot(np.deg2rad(myboat.twa_array), myboat.sail_speed[:,:,0].interp(tws=float(sv.get())))
        print("vitesse" ,myboat.get_sail_interpolated(0, float(sv.get())))
        #print(np.deg2rad(myboat.twa_array))
        ax.plot(np.deg2rad(np.arange(0, 180, 1)),myboat.get_sail_interpolated(0, float(sv.get())))
        graph = FigureCanvasTkAgg(fig, master=polartab)
        canvas = graph.get_tk_widget()
        canvas.grid(row=3)



windspind_level_input.grid(row=1, column=0)

tab_control.add(maptab, text='Carte du vent')
tab_control.pack(expand=1, fill='both')
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
graph = FigureCanvasTkAgg(fig, master=polartab)
canvas = graph.get_tk_widget()
canvas.grid(row=3)"""



"""file_name = get_zezo_grib()
dswind = xr.open_dataset(file_name, engine='cfgrib')
#dswind = dswind.assign(magnitude=(dswind["u10"] ** 2 + dswind["v10"] ** 2) ** 0.5) / 1.94384"""

# polarchart = plt.figure("polarchart")
# polarchart.ax = plt.axes(projection='polar')
# plt.polar(twarad, polarXarray.isel(tws = 1))


# mapmonde = plt.figure("mapmonde")
# mapmonde.ax = plt.axes(projection=ccrs.PlateCarree())
# mapmonde.ax.coastlines(resolution='10m')

# plot = dswind.magnitude.isel(time = 0, step = 0).plot(cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
# ax.barbs(longitude, latitude, dswind.u10.isel(time = 0, step = 0),dswind.u10.isel(time = 0, step = 0), length=3,pivot='middle')


# plt.show()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
