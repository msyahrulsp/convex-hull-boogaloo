def getExtreme(points):
    # [x, y]
    min, max = points[0], points[0]
    minIdx, maxIdx = 0, 0

    for i in range(1, len(points)):
        if (points[i][0] < min[0]):
            min = points[i]
            minIdx = i
        if (points[i][0] > max[0]):
            max = points[i]
            maxIdx = i

    return minIdx, maxIdx

# Fungsi untuk mencari jarak dari garis yang dibentuk oleh p1 dan p2
# dengan titik p3
def distance(p1, p2, p3):
    a = (p2[0] - p1[0]) * (p1[1] - p3[1])
    b = (p1[0] - p3[0]) * (p2[1] - p1[1])
    d = ((p2[0]-p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)
    return((a - b) / d)

# Mencari titik terjauh dari garis p1p2
# Urutan p1 dan p2 berpengaruh
def getFarthest(p1, p2, points):
    max = 0
    maxIdx = -1

    for i in range(len(points)):
        dist = distance(p1, p2, points[i])
        if (max < dist):
            max = dist
            maxIdx = i

    return maxIdx
    

# Rekursi pencarian convexhull
def findHull(p1Idx, p2Idx, points, hull):
    maxIdx = getFarthest(points[p1Idx], points[p2Idx], points)
    
    # Tidak ditemukan titik di luar titik p1 dan p2 
    if (maxIdx == -1):
        hull.append([p1Idx, p2Idx])
        return hull
        
    hull = findHull(p1Idx, maxIdx, points, hull)
    hull = findHull(maxIdx, p2Idx, points, hull)
    return hull

def ConvexHull(points):
    hull = [] # Hanya menerima index untuk memudahkan plotting

    points = points.tolist()
    p1Idx, pnIdx = getExtreme(points)

    hull = findHull(p1Idx, pnIdx, points, hull)
    hull = findHull(pnIdx, p1Idx, points, hull)

    return hull