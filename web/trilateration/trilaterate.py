from math import sqrt, log10

from numpy import array

import basicTrilateration


one_metre_rssi = -45
length = 24.1
width = 18.6


point_data = {
    'HG655D': array([0, 0, 0]),
    '710Nr': array([20, 30, 0]),
    '710Nm': array([0, 60, 0])
}


identifiers = [
    'HG655D',
    '710Nr',
    '710Nm'
]


pythagoras = lambda a, b: sqrt(a**2 + b**2)
rssi_to_distance = lambda rssi: 10**((rssi - one_metre_rssi)/-25.0)
distance_to_rssi = lambda d: -10 * 2.5 * log10(d) + one_metre_rssi


max_rssi = {
    'HG655D': distance_to_rssi(pythagoras(14, width)),
    '710Nr': distance_to_rssi(pythagoras(length, 11.5)),
    '710Nm': distance_to_rssi(pythagoras(17, width))
}


def trilaterate(distance_dict):
    distance_data = [distance_dict[router_id] for router_id in identifiers]
    point_estimate = basicTrilateration.trilaterateLM(point_data, distance_data, identifiers)
    return point_estimate


def trilaterate_rssi(rssi_dict):
    distance_data = [rssi_to_distance(rssi_dict[router_id]) for router_id in identifiers]
    point_estimate = basicTrilateration.trilaterate(point_data, distance_data, identifiers)
    return point_estimate[0], point_estimate[1]