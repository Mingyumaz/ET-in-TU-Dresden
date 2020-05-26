import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#'Display the whole process'
def DisplayWholeProcess(IncidentLight,ReflectionLight,RefractionLight,Plane):
    fig = plt.figure(1)
    ax = fig.gca(projection='3d')
   
#'ploting the lines'
  
    pl_reflection = ReflectionLight.pl
    d_reflection = ReflectionLight.dn
    
    pl_refration = RefractionLight.pl
    d_refration = RefractionLight.dn


    #here we use the Point of incidence on the plane as one point
    #and the other Point is on the basis of the first point, Shift a normalized vector
    #all of the lines will have a length of 1, so the figure will more clear.
    x1 = [-IncidentLight.dn[0]+pl_reflection[0],pl_reflection[0]]
    y1 = [-IncidentLight.dn[1]+pl_reflection[1],pl_reflection[1]]
    z1 = [-IncidentLight.dn[2]+pl_reflection[2],pl_reflection[2]]


    x2 = [pl_reflection[0],d_reflection[0]+pl_reflection[0]]
    y2 = [pl_reflection[1],d_reflection[1]+pl_reflection[1]]
    z2 = [pl_reflection[2],d_reflection[2]+pl_reflection[2]]

    x3 = [pl_refration[0],d_refration[0]+pl_refration[0]]
    y3 = [pl_refration[1],d_refration[1]+pl_refration[1]]
    z3 = [pl_refration[2],d_refration[2]+pl_refration[2]]

    #display the light
    # red is incendent light    
    figure = ax.plot(x1, y1, z1, c='r')
    # blue is reflected lightc
    figure = ax.plot(x2, y2, z2, c='b')
    # yellow is refracted light
    figure = ax.plot(x3, y3, z3, c='y') 
    
#'ploting the plane'
    point_plane  = Plane.po
    normal_plane = Plane.n

    if normal_plane[2] != 0:
        # a plane is a*x+b*y+c*z+d=0
        # [a,b,c] is the normal. Thus, we have to calculate
        # d and we're set
        d = -np.dot(normal_plane,pl_reflection)

        # create x,y
        x = np.arange(pl_reflection[0] - 1,pl_reflection[0] + 1,0.25)
        y = np.arange(pl_reflection[1] - 1,pl_reflection[1] + 1,0.25)
        xx, yy = np.meshgrid(x, y)

        # calculate corresponding z
        z = (-normal_plane[0] * xx - normal_plane[1] * yy - d) * 1. /normal_plane[2]

        surf = ax.plot_surface(xx, yy, z,color = 'gray')

    elif normal_plane[1] != 0:
        #fig = plt.figure()
        ax = fig.gca(projection='3d')

        d = (-normal_plane[0] * pl_reflection[0] - normal_plane[1] * pl_reflection[1]) * np.ones((8,8))
        x = np.arange(pl_reflection[0] - 1,pl_reflection[0] + 1,0.25)
        z = np.arange(pl_reflection[2] - 1,pl_reflection[2] + 1,0.25)
        x, z = np.meshgrid(x, z)
        y = (-d - normal_plane[0] * x) / normal_plane[1]
        surf = ax.plot_surface(x, y, z,color = 'white')

    elif normal_plane[0] != 0:
        #fig = plt.figure()
        ax = fig.gca(projection='3d')

        d = (-normal_plane[0] * pl_reflection[0] ) * np.ones((8,8))
        y = np.arange(pl_reflection[1] - 1,pl_reflection[1] + 1,0.25)
        z = np.arange(pl_reflection[2] - 1,pl_reflection[2] + 1,0.25)
        y, z = np.meshgrid(y, z)
        x = -d / normal_plane[0]
        surf = ax.plot_surface(x, y, z,color = 'white')
    

    ax.set_xlabel(r'$x$',fontsize = 2, color = 'blue')
    ax.set_ylabel(r'$y$',fontsize = 2, color = 'blue')
    ax.set_zlabel(r'$z$',fontsize = 2, color = 'blue')
    plt.show()