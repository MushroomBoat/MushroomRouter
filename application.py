import tkinter as tk
from tkinter import ttk
from utils import *
from boat import Boat
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import cartopy.crs as ccrs


class Application(tk.Frame, Boat):
    def __init__(self, master=None, boat=None):
        super().__init__(master)
        self.master = master
        file_name = 'all.grib'
        #file_name = get_zezo_grib()
        self.dswind = xr.open_dataset(file_name, engine='cfgrib')
        self.dswind = self.dswind.assign(magnitude=(self.dswind["u10"] ** 2 + self.dswind["v10"] ** 2) ** 0.5 * 1.94384)
        self.dswind = self.dswind.assign(
            angle=(np.rad2deg(np.arctan2(self.dswind["u10"], self.dswind["v10"])) + 180) % 360)
        #plt.imshow(self.dswind.magnitude.isel(time=2, step=124), interpolation='bilinear')
        #plt.show()
        self.create_widgets()
        self.create_boat()
        time_index = search_index_lower(get_utctime(), self.dswind.isel(time=-1).valid_time.values)
        #self.create_mapmonde()

    def create_boat(self):
        self.myboat = Boat('boats\mono\class_40.json', FullPack=True)
        # self.myboat.plotpolar(0)
        # self.myboat.plotpolar(1)

    def create_widgets(self):
        self.long_deg = tk.IntVar()
        self.long_min = tk.IntVar()
        self.long_sec = tk.IntVar()
        self.lat_deg = tk.IntVar()
        self.lat_min = tk.IntVar()
        self.lat_sec = tk.IntVar()
        self.long_dest_deg = tk.IntVar()
        self.long_dest_min = tk.IntVar()
        self.long_dest_sec = tk.IntVar()
        self.lat_dest_deg = tk.IntVar()
        self.lat_dest_min = tk.IntVar()
        self.lat_dest_sec = tk.IntVar()
        self.master.title("Welcome to Mushroom Router")
        self.master.geometry('600x700')
        frame_coord_location = tk.Frame(master=self.master)
        self.Current_location_label = tk.Label(master=frame_coord_location, text="Current location:", anchor="w",
                                               width=25).grid(row=0, column=0)
        self.longitude_label = tk.Label(master=frame_coord_location, text="Longitude").grid(row=0, column=1)
        self.entry_longitude_degree = tk.Entry(master=frame_coord_location, fg="blue", width=4,
                                               textvariable=self.long_deg).grid(row=0, column=2)
        self.longitude_deg_unit_label = tk.Label(master=frame_coord_location, text="°").grid(row=0, column=3)
        self.entry_longitude_minute = tk.Entry(master=frame_coord_location, fg="blue", width=2,
                                               textvariable=self.long_min).grid(row=0, column=4)
        self.longitude_minute_unit_label = tk.Label(master=frame_coord_location, text="'").grid(row=0, column=5)
        self.entry_longitude_second = tk.Entry(master=frame_coord_location, fg="blue", width=2,
                                               textvariable=self.long_sec).grid(row=0, column=6)
        self.longitude_second_unit_label = tk.Label(master=frame_coord_location, text="\"").grid(row=0, column=7)

        self.latitude_label = tk.Label(master=frame_coord_location, text="Latitude").grid(row=0, column=8)
        self.entry_latitude_degree = tk.Entry(master=frame_coord_location, fg="blue", width=4,
                                              textvariable=self.lat_deg).grid(row=0, column=9)
        self.latitude_deg_unit_label = tk.Label(master=frame_coord_location, text="°").grid(row=0, column=10)
        self.entry_latitude_minute = tk.Entry(master=frame_coord_location, fg="blue", width=2,
                                              textvariable=self.lat_min).grid(row=0, column=11)
        self.latitude_minute_unit_label = tk.Label(master=frame_coord_location, text="'").grid(row=0, column=12)
        self.entry_latitude_second = tk.Entry(master=frame_coord_location, fg="blue", width=2,
                                              textvariable=self.lat_sec).grid(row=0, column=13)
        self.latitude_second_unit_label = tk.Label(master=frame_coord_location, text="\"").grid(row=0, column=14)

        self.dest_location_label = tk.Label(master=frame_coord_location, text="Destination location:", anchor="w",
                                            width=25).grid(row=1,
                                                           column=0)
        self.longitude_dest_label = tk.Label(master=frame_coord_location, text="Longitude").grid(row=1, column=1)
        self.entry_longitude_dest_degree = tk.Entry(master=frame_coord_location, fg="blue", width=4,
                                                    textvariable=self.long_dest_deg).grid(row=1,
                                                                                          column=2)
        self.longitude_dest_deg_unit_label = tk.Label(master=frame_coord_location, text="°").grid(row=1, column=3)
        self.entry_longitude_dest_minute = tk.Entry(master=frame_coord_location, fg="blue", width=2,
                                                    textvariable=self.long_dest_min).grid(row=1,
                                                                                          column=4)
        self.longitude_dest_minute_unit_label = tk.Label(master=frame_coord_location, text="'").grid(row=1, column=5)
        self.entry_longitude_dest_second = tk.Entry(master=frame_coord_location, fg="blue", width=2,
                                                    textvariable=self.long_dest_sec).grid(row=1,
                                                                                          column=6)
        self.longitude_dest_second_unit_label = tk.Label(master=frame_coord_location, text="\"").grid(row=1, column=7)

        self.latitude_dest_label = tk.Label(master=frame_coord_location, text="Latitude").grid(row=1, column=8)
        self.entry_latitude_dest_degree = tk.Entry(master=frame_coord_location, fg="blue", width=4,
                                                   textvariable=self.lat_dest_deg).grid(row=1,
                                                                                        column=9)
        self.latitude_dest_deg_unit_label = tk.Label(master=frame_coord_location, text="°").grid(row=1, column=10)
        self.entry_latitude_dest_minute = tk.Entry(master=frame_coord_location, fg="blue", width=2,
                                                   textvariable=self.lat_dest_min).grid(row=1,
                                                                                        column=11)
        self.latitude_dest_minute_unit_label = tk.Label(master=frame_coord_location, text="'").grid(row=1, column=12)
        self.entry_latitude_dest_second = tk.Entry(master=frame_coord_location, fg="blue", width=2,
                                                   textvariable=self.lat_dest_sec).grid(row=1,
                                                                                        column=13)
        self.latitude_dest_second_unit_label = tk.Label(master=frame_coord_location, text="\"").grid(row=1, column=14)

        frame_coord_location.pack()

        def submit_coord():
            if (self.long_deg.get() >= -180) and (self.long_deg.get() <= 180):
                self.myboat.current_location[0] = degree_minute_second_to_decimal(self.long_deg.get(),
                                                                                  self.long_min.get(),
                                                                                  self.long_sec.get()) % 360
                self.myboat.current_location[1] = degree_minute_second_to_decimal(self.lat_deg.get(),
                                                                                  self.lat_min.get(),
                                                                                  self.lat_sec.get())
                self.myboat.destination_location[0] = degree_minute_second_to_decimal(self.long_dest_deg.get(),
                                                                                      self.long_dest_min.get(),
                                                                                      self.long_dest_sec.get()) % 360
                self.myboat.destination_location[1] = degree_minute_second_to_decimal(self.lat_dest_deg.get(),
                                                                                      self.lat_dest_min.get(),
                                                                                      self.lat_dest_sec.get())
                print("current location", self.myboat.current_location)
                print("destination location", self.myboat.destination_location)
                self.myboat.navigate(self.dswind)

        # Button navigate
        navigate_button = ttk.Button(master=self.master, text='Navigate', command=submit_coord)
        navigate_button.pack(pady=10)

        def submit_polarspeed():
            self.reset_polar_chart()
            nb = np.shape(self.myboat.sail_speed)
            for i in range(0, nb[2]):
                self.ax.plot(np.deg2rad(np.arange(0, 181, 1)),
                             self.myboat.get_sail_interpolated(self.myboat.sail_speed[:, :, i],
                                                               float(self.windspeed_polar.get())),
                             label=self.myboat.sail_name[i])

            self.ax.plot(np.deg2rad(np.arange(0, 181, 1)),
                         self.myboat.get_sail_interpolated(self.myboat.best_polar_sail,
                                                           float(self.windspeed_polar.get())), "k:", label="All_sail")
            self.ax.legend(bbox_to_anchor=(1.2, 1.05))
            graph = FigureCanvasTkAgg(self.fig1, master=frame1)
            canvas = graph.get_tk_widget()
            canvas.grid(row=4)

        notebook = ttk.Notebook(self.master)
        notebook.pack(pady=1, expand=True)

        # create frames
        frame1 = ttk.Frame(notebook, width=800, height=800)
        frame2 = ttk.Frame(notebook, width=800, height=800)

        self.windspeed_polar = tk.DoubleVar()
        self.windspind_level_label = tk.Label(master=frame1, text="Wind speed : (kts)").grid(row=0, column=0)
        self.windspind_level_input = tk.Entry(master=frame1, fg="blue",
                                              textvariable=self.windspeed_polar).grid(row=1, column=0)

        # Button graph_polar
        graph_polar_button = ttk.Button(master=frame1, text='Validate', command=submit_polarspeed)
        graph_polar_button.grid(row=2, column=0)

        # add frame to interface
        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add notebook to frame 1 and 2
        notebook.add(frame1, text='Polar')
        notebook.add(frame2, text='Map')

        self.fig1 = plt.figure()
        self.ax = self.fig1.add_subplot(projection='polar')
        self.reset_polar_chart()
        graph = FigureCanvasTkAgg(self.fig1, master=frame1)
        canvas = graph.get_tk_widget()
        canvas.grid(row=4)

        self.mapmonde = plt.figure("mapmonde")
        self.mapmonde.ax2 = plt.axes(projection=ccrs.PlateCarree())
        self.mapmonde.ax2.coastlines(resolution='10m')
        #self.dswind.magnitude.isel(time=2, step=1).plot(cmap=plt.cm.nipy_spectral, transform=ccrs.PlateCarree())
        plt.scatter(x=0, y=0, transform=ccrs.PlateCarree())

        graph2 = FigureCanvasTkAgg(self.mapmonde, master=frame2)
        canvas2 = graph2.get_tk_widget()
        tkagg.NavigationToolbar2Tk(graph2, frame2)
        canvas2.pack()




    def create_mapmonde(self):
        mapmonde = plt.figure("mapmonde")
        mapmonde.ax2 = plt.axes(projection=ccrs.PlateCarree())
        mapmonde.ax2.coastlines(resolution='10m')

    def reset_polar_chart(self):
        self.ax.cla()
        self.ax.set_xticks(np.arange(0, np.pi, step=(10 / 360 * 2 * np.pi)))
        self.ax.set_thetamin(0)
        self.ax.set_thetamax(180)
        self.ax.set_theta_zero_location('N')
        self.ax.set_theta_direction(-1)
