import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

import DisplayWholeProcess as DisWP
import DisplayWholeProcess2 as DisWP2

#'The class of light'
class Light(object):
    #'p-Place, d-Direction, NormD-Normalized Direction'
    pl = [0,0,0]
    d = np.array([0,0,0])
    dn = np.array([0,0,0])

    #'set the light verctor'
    def inc(self,place,direction):
        self.pl = place
        self.d = direction
        self.dn = Normalized(direction)

    #'Display the place and direction of the light'
    def displayLight(self):
        print('Display the place and direction of the light: ')
        print('Place:{}, Direction:{}'.format(self.pl,self.dn))

#'The class of Object plane'
class Plane(object):
    #'po-The palce of the point in plane, n-the normal verctor of the plane'
    po = [0,0,0]
    n = np.array([0,1,0])
    nn = np.array([0,1,0])

    #'set the Plane with point and normal verctor'
    def inc(self,point,Normal):
        self.po = point
        self.n = Normal
        self.nn = Normalized(Normal)

    #'display the plane with point/normal verctor and the Equation'
    def displayObjectPlane(self):
        print('display the plane with point/normal verctor')
        print('point:{}, Normal:{}'.format(self.po,self.nn))
        print('display the Equation')
        print('{}(x-{})+{}(y-{})+{}(z-{}) = 0'.format(self.n[0],self.po[0],self.n[1],self.po[1],self.n[2],self.po[2],))

#'put in a verctor[x,y,z],and normalize'
def Normalized(verc):
    #test the function,close to 0 or 0
    #all cases
    x = (np.sqrt(np.square(verc[0])+np.square(verc[1])+np.square(verc[2])))
    if x == 0:
        return [0,0,0]
    else:
        n = 1/ x
        verc = np.dot(verc,n)
        return verc

#'The function to determine if there will be a cross point between the Incidentlight and the plane'
def JudgeCrossPoint(IncidentLight,Plane):
    if np.dot(IncidentLight.d,Plane.n) == 0:
        return False
    else:
        # there is a cross point
        return True

#'The function for reflected light calculation'
def CaRDir(IncidentLight,Plane):
        
    r = np.array([0,0,0])
    
    #'Calculate the direction of the reflected light'
    if abs(round(np.linalg.norm(np.cross(IncidentLight.d,Plane.n)),4)) <= 0.00005:
        #
        #'Special Cases> The incident light is perpendicular to the plane'
        r = np.dot(IncidentLight.d,-1)
    else:
        r = IncidentLight.dn - np.dot(2,np.dot(np.dot(IncidentLight.dn,Plane.nn),Plane.nn))
    return r

#'Calulate the point in the reflected light and the Plane'
def CaPoint(IncidentLight,Plane):
    point = [0,0,0]

    #'vp- The vector of the Plane'
    vpx = Plane.n[0]
    vpy = Plane.n[1]
    vpz = Plane.n[2]
    #'pp- The point of the Plane'
    pp0 = Plane.po[0]
    pp1 = Plane.po[1]
    pp2 = Plane.po[2]

    #'v- the direction of the light'
    v1 = IncidentLight.d[0]
    v2 = IncidentLight.d[1]
    v3 = IncidentLight.d[2]
    #'the place for a point which in the light'
    lp0 = IncidentLight.pl[0]
    lp1 = IncidentLight.pl[1]
    lp2 = IncidentLight.pl[2]
    
    if JudgeCrossPoint(IncidentLight, Plane):
        t = (vpx*(pp0-lp0)+vpy*(pp1-lp1)+vpz*(pp2-lp2))/(vpx*v1+vpy*v2+vpz*v3)
        point[0] = lp0 + v1 * t
        point[1] = lp1 + v2 * t
        point[2] = lp2 + v3 * t
        return point       
    else:
        return False

#'Determine if total reflection will occur'
def JudgeTotalReflection(IncidentLight,Plane,n1,n2):
    if n1 / n2 * np.linalg.norm(np.cross(IncidentLight.dn,Plane.nn)) >= 1:
        #'total internal reflection TIR  --->  False'
        return False
    else:
        #'the transmitted light exist'
        return True

#'Calkulate the direction of the trasmitted light from one medium to the other'
def CaTdir(IncidentLight,Plane,n1,n2):
    #'direction of the transmitted light from n1 to n2'
    d = np.array([0,0,0])

    if JudgeCrossPoint(IncidentLight,Plane):
        if JudgeTotalReflection(IncidentLight,Plane,n1,n2):
            #'make sure the direction will be correct'
            if np.dot(IncidentLight.d,Plane.n) >= 0:
                ind = 1
            else:
                ind = -1
            #'use the equation to calculate the direction of the trasmitted light'
            w = np.cross(np.cross(Plane.nn,IncidentLight.dn),Plane.nn)
            indexN = ind * np.sqrt((np.linalg.norm(IncidentLight.dn))**2 - (np.linalg.norm(w))**2)
            d = np.dot(n1/n2,w) + np.dot(indexN,Plane.nn)
        
    return d

def LightCalFunktion(IncidentLightInput,PlaneInput,n1_Input,n2_Input):
    Reflectedlight_Output = Light()
    Refractedlight_Output = Light()

    if JudgeCrossPoint(IncidentLightInput,PlaneInput):
        # calculate the reflected light and print the point and vector
        Reflectedlight_Output.inc(CaPoint(IncidentLightInput,PlaneInput),CaRDir(IncidentLightInput,PlaneInput))
        #'first judge if the total reflection will happen, Ture is not happen, and False is happen'
        if JudgeTotalReflection(IncidentLightInput,PlaneInput,n1_Input,n2_Input):
            # calculate the transmitted light and print the point and vector
            Refractedlight_Output.inc(CaPoint(IncidentLightInput,PlaneInput),CaTdir(IncidentLightInput,PlaneInput,n1_Input,n2_Input))
        else:            
            # there is no more refractedlight, and then we display IncidentLightInput,Reflectedlight_Output,PlaneInput, 
            # because the default(classLight)set of the direction is [0,0,0]
            # actually we cant see the refractedlight of t 
            Refractedlight_Output.inc([0,0,0],Reflectedlight_Output.n)
    else:
        # There is no cross point, so we set the light as null
        Reflectedlight_Output.inc([0,0,0],[0,0,0])
        Refractedlight_Output.inc([0,0,0],[0,0,0])
    # output the two light
    Reflectedlight_Output.displayLight
    Refractedlight_Output.displayLight
    return [Reflectedlight_Output,Refractedlight_Output]

def DisplayFigure(IncidentLight,Plane,ReflectedLight,RefractedLight):
    if JudgeCrossPoint(IncidentLight,Plane):
        DisWP.DisplayWholeProcess(IncidentLight,ReflectedLight,RefractedLight,Plane)
    else:
        DisWP2.DisplayWholeProcess2(IncidentLight,Plane)
    pass