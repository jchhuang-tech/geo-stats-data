from pykalman import KalmanFilter
import pandas as pd
import sys
import numpy as np
import csv
from pykalman import KalmanFilter
def read_csv(csv_data):
    points = []
    line_count = 0
    with open(csv_data) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # print(row)
                points.append(row)
                line_count += 1
    # print(points)
    df = pd.DataFrame(points, columns=['lat', 'lon'])
    df['lat'] = pd.to_numeric(df['lat'], downcast="float")
    df['lon'] = pd.to_numeric(df['lon'], downcast="float")
    return df


# Adapt from: https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/27943#27943
def distance(points):
    prev_points = points.shift(-1)
    dLat = np.deg2rad(points['lat'] - prev_points['lat'])
    dLon = np.deg2rad(points['lon'] - prev_points['lon'])
    a = np.sin(dLat/2)*np.sin(dLat/2) + \
        np.cos(np.deg2rad(points['lat'])) * np.cos(np.deg2rad(prev_points['lat'])) * \
        np.sin(dLon/2) * np.sin(dLon/2)
    c = np.sum(2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return round(6371000 * c, 6)

def output_gpx(points, output_filename):
    """
    Output a GPX file with latitude and longitude from the points DataFrame.
    """
    from xml.dom.minidom import getDOMImplementation
    def append_trkpt(pt, trkseg, doc):
        trkpt = doc.createElement('trkpt')
        trkpt.setAttribute('lat', '%.8f' % (pt['lat']))
        trkpt.setAttribute('lon', '%.8f' % (pt['lon']))
        trkseg.appendChild(trkpt)

    doc = getDOMImplementation().createDocument(None, 'gpx', None)
    trk = doc.createElement('trk')
    doc.documentElement.appendChild(trk)
    trkseg = doc.createElement('trkseg')
    trk.appendChild(trkseg)

    points.apply(append_trkpt, axis=1, trkseg=trkseg, doc=doc)

    with open(output_filename, 'w') as fh:
        doc.writexml(fh, indent=' ')


# Kalman Filtering
def smooth(points):
    initial_state = points[['lat', 'lon']].iloc[0]
    observation_covariance = np.diag([0.005, 0.005]) ** 2  # TODO: shouldn't be zero
    transition_covariance = np.diag([0.1, 0.1]) ** 2  # TODO: shouldn't be zero
    transition = np.diag([1, 1])  # TODO: shouldn't (all) be zero
    kf = KalmanFilter(initial_state_mean=initial_state,
                      initial_state_covariance=observation_covariance,
                      observation_covariance=observation_covariance,
                      transition_covariance=transition_covariance,
                      transition_matrices=transition)
    kalman_smoothed, _ = kf.smooth(points)
    return pd.DataFrame(kalman_smoothed, columns=['lat', 'lon'])


def main():
    points = read_csv(r'..\353FinalPrj\venv\location.csv')
    # print(points)
    smoothed_points = smooth(points)
    output_gpx(smoothed_points, 'out.gpx')

if __name__ == '__main__':
    main()
