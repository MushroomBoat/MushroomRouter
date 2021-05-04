import tkinter as tk
from tkinter import ttk
from utils import degree_minute_second_to_decimal
from boat import Boat


class Application(tk.Frame, Boat):
    def __init__(self, master=None, boat=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.create_boat()

    def create_boat(self):
        self.myboat = Boat('boats\mono\class_40.json', LightSail=True)

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
        self.master.geometry('600x600')
        frame_coord_location = tk.Frame(master=self.master)
        self.Current_location_label = tk.Label(master=frame_coord_location, text="Current location:", anchor="w",
                                               width=25).grid(row=0, column=0)
        self.longitude_label = tk.Label(master=frame_coord_location, text="Longitude").grid(row=0, column=1)
        self.entry_longitude_degree = tk.Entry(master=frame_coord_location, fg="blue", width=4, textvariable=self.long_deg).grid(row=0, column=2)
        self.longitude_deg_unit_label = tk.Label(master=frame_coord_location, text="°").grid(row=0, column=3)
        self.entry_longitude_minute = tk.Entry(master=frame_coord_location, fg="blue", width=2, textvariable=self.long_min).grid(row=0, column=4)
        self.longitude_minute_unit_label = tk.Label(master=frame_coord_location, text="'").grid(row=0, column=5)
        self.entry_longitude_second = tk.Entry(master=frame_coord_location, fg="blue", width=2, textvariable=self.long_sec).grid(row=0, column=6)
        self.longitude_second_unit_label = tk.Label(master=frame_coord_location, text="\"").grid(row=0, column=7)

        self.latitude_label = tk.Label(master=frame_coord_location, text="Latitude").grid(row=0, column=8)
        self.entry_latitude_degree = tk.Entry(master=frame_coord_location, fg="blue", width=4, textvariable=self.lat_deg).grid(row=0, column=9)
        self.latitude_deg_unit_label = tk.Label(master=frame_coord_location, text="°").grid(row=0, column=10)
        self.entry_latitude_minute = tk.Entry(master=frame_coord_location, fg="blue", width=2, textvariable=self.lat_min).grid(row=0, column=11)
        self.latitude_minute_unit_label = tk.Label(master=frame_coord_location, text="'").grid(row=0, column=12)
        self.entry_latitude_second = tk.Entry(master=frame_coord_location, fg="blue", width=2, textvariable=self.lat_sec).grid(row=0, column=13)
        self.latitude_second_unit_label = tk.Label(master=frame_coord_location, text="\"").grid(row=0, column=14)

        self.dest_location_label = tk.Label(master=frame_coord_location, text="Destination location:", anchor="w",
                                            width=25).grid(row=1,
                                                           column=0)
        self.longitude_dest_label = tk.Label(master=frame_coord_location, text="Longitude").grid(row=1, column=1)
        self.entry_longitude_dest_degree = tk.Entry(master=frame_coord_location, fg="blue", width=4, textvariable=self.long_dest_deg).grid(row=1,
                                                                                                          column=2)
        self.longitude_dest_deg_unit_label = tk.Label(master=frame_coord_location, text="°").grid(row=1, column=3)
        self.entry_longitude_dest_minute = tk.Entry(master=frame_coord_location, fg="blue", width=2, textvariable=self.long_dest_min).grid(row=1,
                                                                                                          column=4)
        self.longitude_dest_minute_unit_label = tk.Label(master=frame_coord_location, text="'").grid(row=1, column=5)
        self.entry_longitude_dest_second = tk.Entry(master=frame_coord_location, fg="blue", width=2, textvariable=self.long_dest_sec).grid(row=1,
                                                                                                          column=6)
        self.longitude_dest_second_unit_label = tk.Label(master=frame_coord_location, text="\"").grid(row=1, column=7)

        self.latitude_dest_label = tk.Label(master=frame_coord_location, text="Latitude").grid(row=1, column=8)
        self.entry_latitude_dest_degree = tk.Entry(master=frame_coord_location, fg="blue", width=4, textvariable=self.lat_dest_deg).grid(row=1,
                                                                                                         column=9)
        self.latitude_dest_deg_unit_label = tk.Label(master=frame_coord_location, text="°").grid(row=1, column=10)
        self.entry_latitude_dest_minute = tk.Entry(master=frame_coord_location, fg="blue", width=2, textvariable=self.lat_dest_min).grid(row=1,
                                                                                                         column=11)
        self.latitude_dest_minute_unit_label = tk.Label(master=frame_coord_location, text="'").grid(row=1, column=12)
        self.entry_latitude_dest_second = tk.Entry(master=frame_coord_location, fg="blue", width=2, textvariable=self.lat_dest_sec).grid(row=1,
                                                                                                         column=13)
        self.latitude_dest_second_unit_label = tk.Label(master=frame_coord_location, text="\"").grid(row=1, column=14)

        frame_coord_location.pack()

        def submit_coord():
            if (self.long_deg.get() >= -180) and (self.long_deg.get() <= 180):
                self.myboat.current_location[0] = degree_minute_second_to_decimal(self.long_deg.get(),
                                                                                  self.long_min.get(),
                                                                                  self.long_sec.get())
                self.myboat.current_location[1] = degree_minute_second_to_decimal(self.lat_deg.get(),
                                                                                  self.lat_min.get(),
                                                                                  self.lat_sec.get())
                self.myboat.destination_location[0] = degree_minute_second_to_decimal(self.long_dest_deg.get(),
                                                                                  self.long_dest_min.get(),
                                                                                  self.long_dest_sec.get())
                self.myboat.destination_location[1] = degree_minute_second_to_decimal(self.lat_dest_deg.get(),
                                                                                  self.lat_dest_min.get(),
                                                                                  self.lat_dest_sec.get())
                print("current location", self.myboat.current_location)
                print("destination location", self.myboat.destination_location)
                # ax.plot(np.deg2rad(myboat.twa_array), myboat.sail_speed[:,:,0].interp(tws=float(sv.get())))
                #print("vitesse", myboat.get_sail_interpolated(0, float(sv.get())))
                # print(np.deg2rad(myboat.twa_array))
                #ax.plot(np.deg2rad(np.arange(0, 180, 1)), myboat.get_sail_interpolated(0, float(sv.get())))
                #graph = FigureCanvasTkAgg(fig, master=polartab)
                #canvas = graph.get_tk_widget()
                #canvas.grid(row=3)

        # Button submit
        submit_button = ttk.Button(master = self.master, text='Navigate', command=submit_coord)
        submit_button.pack()
        #windspind_level_input = ttk.Entry(polartab, textvariable=sv)

        notebook = ttk.Notebook(self.master)
        notebook.pack(pady=1, expand=True)

        # create frames
        frame1 = ttk.Frame(notebook, width=600, height=600)
        frame2 = ttk.Frame(notebook, width=600, height=600)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add frames to notebook

        notebook.add(frame1, text='Polar')
        notebook.add(frame2, text='Map')

        # tab_control = ttk.notebook
        # polartab = tk.Frame(tab_control)
        # maptab = tk.Frame(tab_control)
        # tab_control.add(polartab, text='Polaire')
        # tk.Label(polartab, text="Wind speed (kts)").grid(row=0, column=0)

