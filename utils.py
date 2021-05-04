def search_index_lower(x, array):
    index = 0
    while array[index] < x:
        index = index + 1
    return index - 1


# https://fr.wikipedia.org/wiki/Interpolation_bilin%C3%A9aire
def interp2d_linear(x, y, array_x, array_y, data):
    x1 = search_index_lower(x, array_x)
    x2 = x1 + 1
    y1 = search_index_lower(y, array_y)
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
