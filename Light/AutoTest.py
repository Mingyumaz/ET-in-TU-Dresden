import numpy as np
import random

import FunktionLight as Fun

#'The optical path is reversible'

#'This programm need circulation'
#'as a human, we can not one by one to set all the cases, and one by one check the corectness'

#'If the total reflection will occur, then we set the direction of transmitted light as [0,0,0],(because the default set is [0,0,0]) 
# and so we cant use the reversible to prove the corectness'
#'But we assume the reflected light always exsit, so we can prove the corectness of reflected light'

def AutoCheckTest(IncidentLight,Plane,ReflectedLight,TrasmittedLight,n1,n2):
    #'use the Reflectedlight to calculate the Incidentlight'
    r2 = np.array([0,0,0])
    r2 = Fun.CaRDir(ReflectedLight,Plane)


    #'use the Trasmitted light to calculate the Incidentlight'
    t2 = np.array([0,0,0])
    t2 = Fun.CaTdir(TrasmittedLight,Plane,n2,n1)
    

    if abs(np.linalg.norm(np.cross(IncidentLight.dn,r2))) <= 0.1:
        print('yes')
    else:
        print('-------->  R false for this point:--------<')
        IncidentLight.displayLight()
        print(r2)
        return False
    
    if abs(np.linalg.norm(np.cross(IncidentLight.dn,t2))) <= 0.1:
        print('ok')
    else:
        print('-------->  T false for this point:--------<')
        IncidentLight.displayLight()
        print('n1 : n2')
        print(n1,n2)
        print(t2)
        return False

    return True

def RandomLightInput():    
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane


    a.inc(np.random.randn(3),np.random.randn(3))
    b.inc(np.random.randn(3),np.random.randn(3))
    n1 = np.random.randint(1,3)
    n2 = np.random.randint(1,3)

    return (a,b,n1,n2)