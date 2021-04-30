import xarray as xr
import matplotlib.pyplot as plt

from math import *
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from boat import *
from utils import *

myboat = Boat(Foil=True)
myboat.read('boats\mono\class_40.json')

print("foilfactor : ", myboat.foil.foiling_factor(14, 100))
print("sailname : ", myboat.sail_name)
print("sailspeed : ", myboat.sail_speed[:,:,0])
polarXarray = xr.Dataset({
        "spi": (["twa", "tws"], myboat.sail_speed[:,:,1]),
        "jib": (["twa", "tws"], myboat.sail_speed[:,:,0]),
    },
    coords={
        "twa": (myboat.twa_array),
        "tws": (myboat.tws_array),
    },
)

speed =myboat.get_speed_sail(10,25,myboat.sail_speed[:,:,0])
print("speed", speed)


polarXarray = xr.DataArray(myboat.sail_speed[:,:,0], dims=("twa", "tws"), name="toto", coords={"twa": myboat.twa_array, "tws": myboat.tws_array})
#print(polarXarray)

def get_zezo_grib():
    import wget
    import os
    if os.path.exists('all.grib'):
        os.remove('all.grib')
    urlzezo = "http://zezo.org/grib/gribv1/all.grib"
    result = wget.download(urlzezo, 'all.grib')
    print("Grib téléchargé")
    return result


window = Tk()
window.title("Welcome to Mushroom Router")
window.geometry('600x600')
tab_control = ttk.Notebook(window)
polartab = ttk.Frame(tab_control)
maptab = ttk.Frame(tab_control)
tab_control.add(polartab, text='Polaire')
ttk.Label(polartab, text="Wind speed (kts)").grid(row=0, column=0)
sv = StringVar()


def submit_polar():
    if (float(sv.get()) >= 0) and (float(sv.get()) <= 17):
        ax.plot(np.deg2rad(myboat.twa_array), polarXarray.interp(tws=float(sv.get())))
        graph = FigureCanvasTkAgg(fig, master=polartab)
        canvas = graph.get_tk_widget()
        canvas.grid(row=3)


# Button submit
submit_button = ttk.Button(polartab, text='Submit', command=submit_polar)
submit_button.grid(column=0, row=2)

# sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
windspind_level_input = ttk.Entry(polartab, textvariable=sv)

windspind_level_input.grid(row=1, column=0)

tab_control.add(maptab, text='Carte du vent')
tab_control.pack(expand=1, fill='both')
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
# ax.plot(np.deg2rad(boat.twa), polarXarray.isel(tws = 1))
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
graph = FigureCanvasTkAgg(fig, master=polartab)
canvas = graph.get_tk_widget()
canvas.grid(row=3)

window.mainloop()

"""file_name = get_zezo_grib()
dswind = xr.open_dataset(file_name, engine='cfgrib')
dswind = dswind.assign(magnitude=(dswind["u10"] ** 2 + dswind["v10"] ** 2) ** 0.5) / 1.94384
longitude = dswind.longitude
latitude = dswind.latitude
print(dswind)"""

# polarchart = plt.figure("polarchart")
# polarchart.ax = plt.axes(projection='polar')
# plt.polar(twarad, polarXarray.isel(tws = 1))



#mapmonde = plt.figure("mapmonde")
#mapmonde.ax = plt.axes(projection=ccrs.PlateCarree())
#mapmonde.ax.coastlines(resolution='10m')

#plot = dswind.magnitude.isel(time = 0, step = 0).plot(cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
#ax.barbs(longitude, latitude, dswind.u10.isel(time = 0, step = 0),dswind.u10.isel(time = 0, step = 0), length=3,pivot='middle')


# plt.show()
