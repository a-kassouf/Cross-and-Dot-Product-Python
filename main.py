import numpy


#3 coordinates
coordA = input("input coords of A in the format [x,y,z]: ")
coordB = input("input coords of B in the format [x,y,z]: ")
coordC = input("input coords of C in the format [x,y,z]: ")
coordD = input("input coords of D in the format [x,y,z]: ")

#coordA = "[1,2,3]"
#coordB = "[2,-2,5]"
#coordC = "[0,0,0]"
#coordD = "[-1,-5,9]"
def splitAndFix(Coord):
    noArcCoord = ""
    for i in Coord:
        if (i != "["):
            if (i != "]"):
                noArcCoord += i
    CoordReturn = list(noArcCoord.split(","))
    return CoordReturn



a = splitAndFix(coordA)
b = splitAndFix(coordB)
c = splitAndFix(coordC)
d = splitAndFix(coordD)

def VectorMake (Coord2, Coord1):
    vectorCoords = [(int(Coord1[0])-int(Coord2[0])),(int(Coord1[1])-int(Coord2[1])),(int(Coord1[2])-int(Coord2[2]))]
    return vectorCoords

#triange 2d
AB = VectorMake(a,b)
AC = VectorMake(a,c)
BC = VectorMake(b,c)

#tetrahedron 3d
AD = VectorMake(a,d)
BD = VectorMake(b,d)
CD = VectorMake(c,d)

print("AB: ", AB)
print("AC: ", AC)
print("BC: ", BC)

print ("ABxAC: ", numpy.cross(AB, AC))
print ("ABxBC: ", numpy.cross(AB, BC))
print ("ACxBC: ", numpy.cross(BC, AC))

print ("AD.ABxAC: ", numpy.dot(AD, numpy.cross(AB, AC)))
print ("BD.ABxAC: ", numpy.dot(BD, numpy.cross(AB, AC)))
print ("CD.ABxAC: ", numpy.dot(CD, numpy.cross(AB, AC)))
