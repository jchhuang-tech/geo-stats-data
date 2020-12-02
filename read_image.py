import os
import exifread
import re
import sys
import csv
import requests
import json
# https://blog.csdn.net/qq_39146974/article/details/103054022
# traverse each folder all the image to read exif information
def get_image_GPS(pic_dir):
    # print(pic_dir)
    items = os.listdir(pic_dir)
    points = []
    for item in items:
        path = os.path.join(pic_dir, item)
        if os.path.isdir(path):
            get_image_GPS(path)
        else:
            points.append(image_read(path))
    write_to_csv(points)
def image_read(path):
    f = open(path, 'rb')
    GPS = {}
    try:
        tag = exifread.process_file(f)
    except:
        return
    if 'GPS GPSLatitude' in tag:
        lat = str(tag['GPS GPSLatitude'])
        if lat == '[0, 0, 0]' or lat == '[0/0, 0/0, 0/0]':
            return
        deg, minu, sec = [x.replace(' ', '') for x in lat[1:-1].split(',')]
        GPS['GPSLatitude'] = convert_to_decimal(deg, minu,sec)

    if 'GPS GPSLongitude' in tag:
        lng = str(tag['GPS GPSLongitude'])
        if lng == '[0, 0, 0]' or lng == '[0/0, 0/0, 0/0]':
            return
        deg, minu, sec = [x.replace(' ', '') for x in lng[1:-1].split(',')]
        GPS['GPSLongitude'] = -convert_to_decimal(deg, minu,sec)

    if 'GPSLatitude' in GPS:
        return [GPS['GPSLatitude'], GPS['GPSLongitude']]

def write_to_csv(points):
    path = "location.csv"
    csv_head = ["Latitude", "Longitude"]
    # Fix the extra space
    with open(path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(csv_head)
        csvwriter.writerows(points)

def convert_to_decimal(*gps):
    # degree
    if '/' in gps[0]:
        deg = gps[0].split('/')
        if deg[0] == '0' or deg[1] == '0':
            gps_d = 0
        else:
            gps_d = float(deg[0]) / float(deg[1])
    else:
        gps_d = float(gps[0])
    # minutes
    if '/' in gps[1]:
        minu = gps[1].split('/')
        if minu[0] == '0' or minu[1] == '0':
            gps_m = 0
        else:
            gps_m = (float(minu[0]) / float(minu[1])) / 60
    else:
        gps_m = float(gps[1]) / 60
    # second
    if '/' in gps[2]:
        sec = gps[2].split('/')
        if sec[0] == '0' or sec[1] == '0':
            gps_s = 0
        else:
            gps_s = (float(sec[0]) / float(sec[1])) / 3600
    else:
        gps_s = float(gps[2]) / 3600

    return gps_d + gps_m + gps_s

if __name__ == "__main__":
    get_image_GPS(r"..\CMPT353\353FinalPrj\Prj image")
