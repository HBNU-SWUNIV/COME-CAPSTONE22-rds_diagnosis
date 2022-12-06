import pydicom
import numpy as np
import math


def dcm2png(dcm_filepath):
    dcm = pydicom.dcmread(dcm_filepath, force=True)
    dcm.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian  # or whatever is the correct transfer syntax for the file
    arr = dcm.pixel_array
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    scaled_arr = (arr - arr_min) / arr_max * 255.0  # normalize to [0, 255]
    scaled_arr = np.asarray(scaled_arr, dtype=np.uint8)

    return scaled_arr


# Shoelace formula to calculate the area of a polygon
# the points must be sorted anticlockwise (or clockwise)
def polygon_area(vertices):
    psum = 0
    nsum = 0

    for i in range(len(vertices)):
        sindex = (i + 1) % len(vertices)
        prod = vertices[i][0] * vertices[sindex][1]
        psum += prod

    for i in range(len(vertices)):
        sindex = (i + 1) % len(vertices)
        prod = vertices[sindex][0] * vertices[i][1]
        nsum += prod

    return abs(1 / 2 * (psum - nsum))


# returns the average x and y coordinates of all the points
def average_point_inside(points):
    x = 0
    y = 0
    for point in points:
        x += point[0]
        y += point[1]
    return x / len(points), y / len(points)


# returns the angle made by a line segment
# connecting p1 and p2 with x-axis in the anticlockwise direction
def angle(p1, p2):
    k = (p2[1] - p1[1]) / math.dist(p1, p2)

    x2 = p2[0]
    x1 = p1[0]

    if k >= 0:
        if x2 >= x1:  # First Quadrant
            return (2.0 * math.pi - math.asin(k))
        else:  # Second Quadrant
            return (math.pi + math.asin(k))
    else:
        if x2 >= x1:  # Fourth Quadrant
            return math.asin(-k)
        else:  # Third Quadrant
            return (math.pi - math.asin(-k))


# angularly sort the points anticlockwise
def sort_angular(points, reference_point):
    return sorted(points, key=lambda point: -angle(point, reference_point))

