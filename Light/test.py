import numpy as np
import math

import FunktionLight as Fun

#'here we give the test case'

#'the Incident light is paralle to the Plane'
def InputLightPlane1():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([1,2,-3],[2,1,2])
    b.inc([0,0,0],[-1,4,-1])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'the Incident light is verticale to the Plane'
def InputLightPlane2():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([1,2,-3],[2,1,2])
    b.inc([0,0,0],[2,1,2])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'the Incident light is nearly paralle to the Plane'
def InputLightPlane3():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([1,0,0],[2,1,2])
    b.inc([0,0,0],[-1,4,-0.9])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'the Incident light is nearly verticale to the Plane'
def InputLightPlane4():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([1,2,-3],[2,1,1.999])
    b.inc([0,0,0],[2,1,2])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'the incident light verctor is [0,0,0]'
def InputLightPlane5():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([1,2,-3],[0,0,0])
    b.inc([0,0,0],[2,1,2])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'the Plane verctor is [0,0,0]'
def InputLightPlane6():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([1,2,-3],[2,1,1])
    b.inc([0,0,0],[0,0,0])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'case'
def InputLightPlane7():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([1,2,-3],[2,1,4])
    b.inc([0,0,0],[2,4,3])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)
    
# 'Total reflection'
def InputLightPlane8():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([1,2,-3],[2,1,4])
    b.inc([0,0,0],[2,4,3])   
    n1 = 9
    n2 = 1
    return (a,b,n1,n2)


#'Test 1 Total reflection'
def InputLightPlane9():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([-1,1,0],[1,-1,0])
    b.inc([0,0,0],[0,1,0])   
    n1 = math.sqrt(2)
    n2 = 1
    return (a,b,n1,n2)

#'Test vertical'
def InputLightPlane10():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([0,1,0],[0,-1,0])
    b.inc([0,0,0],[0,1,0])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'Test nearly vertical'
def InputLightPlane11():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([-1,50,0],[-1,-50,0])
    b.inc([0,0,0],[0,1,0])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'Test nearly vertical'
def InputLightPlane12():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([0,1,0],[1,1,0])
    b.inc([0,0,0],[1,-1,0])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

#'Test zero'
def InputLightPlane13():
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc([0,0,0],[0,0,0])
    b.inc([0,0,0],[0,1,0])   
    n1 = 1
    n2 = 1
    return (a,b,n1,n2)

