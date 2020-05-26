import FunktionLight as Fun    # The code to test
import numpy as np
import math

def test1():
    a = Fun.Light()# a is Incident light
    b = Fun.Plane()# b is the Plane
    #The input of Function
    a.inc([-1,1,0],[1,-1,0])
    b.inc([0,0,0],[0,1,0])
    n1 = math.sqrt(2)
    n2 = 1
    #The output should be

    r1 = (Fun.CaRDir(a,b) == Fun.Normalized(np.array([1,1,0]))).all()
    r2 = (Fun.CaPoint(a,b) == np.array([0,0,0])).all()
    r3 = (Fun.CaTdir(a,b,n1,n2) == Fun.Normalized(np.array([0,0,0]))).all()
    assert r1 & r2 & r3

# The incidentlight is vertical to the plane
def test2():
    a = Fun.Light()# a is Incident light
    b = Fun.Plane()# b is the Plane
    #The input of Function
    a.inc([0,1,0],[0,-1,0])
    b.inc([0,0,0],[0,1,0])
    n1 = 1
    n2 = 1
    #The output should be

    r1 = (Fun.CaRDir(a,b) == Fun.Normalized(np.array([0,1,0]))).all()
    r2 = (Fun.CaPoint(a,b) == np.array([0,0,0])).all()
    r3 = (Fun.CaTdir(a,b,n1,n2) == Fun.Normalized(np.array([0,-1,0]))).all()
    assert r1 & r2 & r3

# The incidentlight is Null
def test3():
    a = Fun.Light()# a is Incident light
    b = Fun.Plane()# b is the Plane
    #The input of Function
    a.inc([0,0,0],[0,0,0])
    b.inc([0,0,0],[0,1,0])
    n1 = 1
    n2 = 1
    #The output should be

    r1 = (Fun.JudgeCrossPoint(a,b) == False)
    assert r1

# The incidentlight is parallel to the plane
def test4():
    a = Fun.Light()# a is Incident light
    b = Fun.Plane()# b is the Plane
    #The input of Function
    a.inc([0,1,0],[1,1,0])
    b.inc([0,0,0],[-1,1,0])
    n1 = 1
    n2 = 1
    #The output should be

    r2 = Fun.CaPoint(a,b) == False
    assert r2
