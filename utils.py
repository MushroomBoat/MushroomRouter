from datetime import datetime
from math import radians, fabs, cos, sin, atan2, sqrt
import numpy as np


def get_utctime():
    dt = datetime.utcnow()
    dt64 = np.datetime64(dt)
    return dt64


def search_index_lower(x, array):
    index = 0
    #print('array_lenght', len(array))
    #print('x', x)
    #print('array', array)
    while array[index] <= x and len(array) > index+1:
        if len(array) > index+1:
            index = index + 1
    #print('index', index)
    return index - 1


# https://fr.wikipedia.org/wiki/Interpolation_bilin%C3%A9aire
def interp2d_linear(x, y, array_x, array_y, data):
    #print('x', x)
    #print('array_x', array_x)

    #print('y', y)
    #print('array_y', array_y)

    x1 = search_index_lower(x, array_x)
    #print('x1', x1)
    #print('array_x1', array_x[x1])
    x2 = x1 + 1
    y1 = search_index_lower(y, array_y)
    #print('y1', y1)
    #print('array_y1', array_y[y1])
    y2 = y1 + 1
    dx = x - array_x[x1]
    dy = y - array_y[y1]
    delta_x = array_x[x2] - array_x[x1]
    delta_y = array_y[y2] - array_y[y1]
    delta_fx = data[x2][y1] - data[x1][y1]
    delta_fy = data[x1][y2] - data[x1][y1]
    delta_fxy = data[x1][y1] + data[x2][y2] - data[x2][y1] - data[x1][y2]
    result = delta_fx * (dx / delta_x) + delta_fy * (dy / delta_y) + delta_fxy * (dx * dy / (delta_x * delta_y)) + \
             data[x1][y1]
    return result


def degree_minute_second_to_decimal(degree, minute, second):
    if degree >= 0:
        result = degree + minute / 60 + second / 3600
    else:
        result = degree - minute / 60 - second / 3600
    return result


def get_zezo_grib():
    import wget
    import os
    if os.path.exists('all.grib'):
        os.remove('all.grib')
    url_zezo = "http://zezo.org/grib/gribv1/all.grib"
    result = wget.download(url_zezo, 'all.grib')
    print("Grib téléchargé")
    return result


# https://en.wikipedia.org/wiki/Trilinear_interpolation
def get_wind_speed(latitude, longitude, time, gribdataset):
    offset = 0
    time_index = search_index_lower(time, gribdataset.isel(time=-1).valid_time.values)

    # if not find in last data time, find them in the previous data time
    if time_index == -1:
        offset = 1
        time_index = search_index_lower(time, gribdataset.isel(time=-2).valid_time.values)

    previous_time = gribdataset.isel(time=-1 - offset, step=time_index).valid_time.values
    next_time = gribdataset.isel(time=-1, step=time_index + 1 - 2 * offset).valid_time.values
    wind_speed_previous_time = interp2d_linear(-latitude, longitude, -gribdataset.latitude.values,
                                               gribdataset.longitude.values,
                                               gribdataset.magnitude.isel(time=-1 - offset, step=time_index)).values
    wind_angle_previous_time = interp2d_linear(-latitude, longitude, -gribdataset.latitude.values,
                                               gribdataset.longitude.values,
                                               gribdataset.angle.isel(time=-1 - offset, step=time_index)).values
    wind_speed_next_time = interp2d_linear(-latitude, longitude, -gribdataset.latitude.values,
                                           gribdataset.longitude.values,
                                           gribdataset.magnitude.isel(time=-1, step=time_index + 1 - 2 * offset)).values
    wind_angle_next_time = interp2d_linear(-latitude, longitude, -gribdataset.latitude.values,
                                           gribdataset.longitude.values,
                                           gribdataset.angle.isel(time=-1, step=time_index + 1 - 2 * offset)).values
    time_factor = (time - previous_time) / (next_time - previous_time)
    wind_speed_interp = wind_speed_previous_time * (1 - time_factor) + wind_speed_next_time * time_factor
    wind_angle_interp = wind_angle_previous_time * (1 - time_factor) + wind_angle_next_time * time_factor
    # print('wind_angle_previous_time :', previous_time, wind_angle_previous_time)
    # print('wind_angle_next_time :', next_time, wind_angle_next_time)
    print('wind_angle_previous_time :', previous_time, wind_angle_previous_time)
    print('wind_angle_next_time :', next_time, wind_angle_next_time)
    print('wind_speed_previous_time :', previous_time, wind_speed_previous_time)
    print('wind_speed_next_time', next_time, wind_speed_next_time)
    return wind_speed_interp, wind_angle_interp


#
# Rayon de la Terre au niveau de l'équateur (en mètres)
# a = 6378137
#
# Rayon de la Terre au niveau des pôles (en mètres)
# b = 6356752
#
# Rayon moyen de la Terre (en mètres)
# R = (2*a+b)/3 = 6371009
#
def great_circle_distance(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dLon = radians(fabs(lon2 - lon1))

    cosLat1 = cos(lat1)
    sinLat1 = sin(lat1)
    cosLat2 = cos(lat2)
    sinLat2 = sin(lat2)
    cosDLon = cos(dLon)
    sinDLon = sin(dLon)

    A = cosLat2 * sinDLon
    B = cosLat1 * sinLat2 - sinLat1 * cosLat2 * cosDLon

    return 6371009 * atan2(sqrt(A * A + B * B),
                           sinLat1 * sinLat2 + cosLat1 * cosLat2 * cosDLon)
