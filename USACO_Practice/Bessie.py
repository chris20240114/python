Billboard1 = {'x1':1, 'y1':2, 'x2':3, 'y2':5}
Billboard2 = {'x1':6, 'y1':0, 'x2':10, 'y2':4}
Truck = {'x1':2, 'y1':1, 'x2':8, 'y2':3}

def calculate_area(x1, y1, x2, y2):
    return (x2-x1)*(y2-y1)
def visible_area1(billboardcoords, truckcoords):
    overlap_coordinatex1 = None
    overlap_coordinatey1 = None
    overlap_coordinatex2 = None
    overlap_coordinatey2 = None
    visiblearea = None
    # if truckcoords['x1']<=billboardcoords['x1'] and truckcoords['y1']<=billboardcoords['y1'] and truckcoords['x2']>=billboardcoords['x2'] and truckcoords['y2']>=billboardcoords['y2']:
    #     visiblearea = 0
    if truckcoords['x1']<=billboardcoords['x1']:
        #set the x coord of the calculation point to billboard1[x1]
        overlap_coordinatex1 = billboardcoords['x1']
        print(overlap_coordinatex1)
    elif not(truckcoords['x1']<=billboardcoords['x1']):
        overlap_coordinatex1 = truckcoords['x1']
        print(overlap_coordinatex1)
    if truckcoords['y1']>=billboardcoords['y1']:
        overlap_coordinatey1 = truckcoords['y1']
        print(overlap_coordinatey1)
    elif not (truckcoords['y1']>=billboardcoords['y1']):
        overlap_coordinatey1 = billboardcoords['y1']
        print(overlap_coordinatey1)
    if truckcoords['x2']>= billboardcoords['x2']:
        overlap_coordinatex2 = billboardcoords['x2']
    elif not(truckcoords['x2']>= billboardcoords['x2']):
        overlap_coordinatex2 = truckcoords['x2']
    if truckcoords['y2']>=billboardcoords['y2']:
        overlap_coordinatey2 = billboardcoords['y2']
        print(overlap_coordinatey2)
    elif not (truckcoords['y2']>=billboardcoords['y2']):
        overlap_coordinatey2 = truckcoords['y2']
        print(overlap_coordinatey2)

    billboard_area = calculate_area(billboardcoords['x1'], billboardcoords['y1'], billboardcoords['x2'], billboardcoords['y2'])
    visiblearea = billboard_area - calculate_area(overlap_coordinatex1, overlap_coordinatey1, overlap_coordinatex2, overlap_coordinatey2)
    print(visiblearea)
    return visiblearea

area1 = visible_area1(Billboard1, Truck)
area2 = visible_area1(Billboard2, Truck)
print(area1+area2)
# Billboard1_area = calculate_area(Billboard1['x1'],  Billboard1['y1'], Billboard1['x2'], Billboard1['y2'])
# print(Billboard1_area)
# Billboard2_area = calculate_area(Billboard2['x1'], Billboard2['y1'], Billboard2['x2'], Billboard2['y2'])
# print(Billboard2_area)

# Billboard1_overlap = calculate_area(Truck['x1'], Billboard1['y1'], Billboard1['x2'], Truck['y2'])
# Billboard2_overlap = calculate_area(Billboard2['x1'], Truck['y1'], Truck['x2'], Truck['y2'])

# visible_area = Billboard1_area + Billboard2_area - Billboard1_overlap - Billboard2_overlap
# print(visible_area)