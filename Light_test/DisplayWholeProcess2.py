import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#'Display the whole process when the incident light is parallel to the plane'
def DisplayWholeProcess2(IncidentLight,Plane):
    fig = plt.figure(1)
    ax = fig.gca(projection='3d')
    
    #'ploting the line'
    pl_incident = IncidentLight.pl
    d_incident = IncidentLight.d
    
    x1 = [pl_incident[0],pl_incident[0] + d_incident[0]]
    y1 = [pl_incident[1],pl_incident[1] + d_incident[1]]
    z1 = [pl_incident[2],pl_incident[2] + d_incident[2]]
    
    figure = ax.plot(x1, y1, z1, c='r')
    
    #'ploting the plane'
    point_plane  = Plane.po
    normal_plane = Plane.n

    if normal_plane[2] != 0:
        # a plane is a*x+b*y+c*z+d=0
        # [a,b,c] is the normal. Thus, we have to calculate
        # d and we're set
        d = -np.dot(normal_plane,point_plane)

        # create x,y
        x = np.arange(point_plane[0] - 5,point_plane[0] + 5,0.25)
        y = np.arange(point_plane[1] - 5,point_plane[1] + 5,0.25)
        xx, yy = np.meshgrid(x, y)

        # calculate corresponding z
        z = (-normal_plane[0] * xx - normal_plane[1] * yy - d) * 1. /normal_plane[2]

        surf = ax.plot_surface(xx, yy, z,color = 'gray')

    elif normal_plane[1] != 0:
        #fig = plt.figure()
        #ax = fig.gca(projection='3d')

        d = (-normal_plane[0] * point_plane[0] - normal_plane[1] * point_plane[1]) * np.ones((40,40))
        x = np.arange(point_plane[0] - 5,point_plane[0] + 5,0.25)
        z = np.arange(point_plane[2] - 5,point_plane[2] + 5,0.25)
        x, z = np.meshgrid(x, z)
        y = (-d - normal_plane[0] * x) / normal_plane[1]
        surf = ax.plot_surface(x, y, z,color = 'white')

    elif normal_plane[0] != 0:
        #fig = plt.figure()
        #ax = fig.gca(projection='3d')

        d = (-normal_plane[0] * point_plane[0] ) * np.ones((40,40))
        y = np.arange(point_plane[1] - 5,point_plane[1] + 5,0.25)
        z = np.arange(point_plane[2] - 5,point_plane[2] + 5,0.25)
        y, z = np.meshgrid(y, z)
        x = -d / normal_plane[0]
        surf = ax.plot_surface(x, y, z,color = 'white')
    


    ax.set_xlabel(r'$x$',fontsize = 20, color = 'blue')
    ax.set_ylabel(r'$y$',fontsize = 20, color = 'blue')
    ax.set_zlabel(r'$z$',fontsize = 20, color = 'blue')
    plt.show()

