
#import main modules
import bpy
import bmesh
import random
import numpy as np



class Walk2d_massive():
    def __init__(self,number_of_walk):
        self.number_of_walk = number_of_walk 
    def random_walk_algorytm(self):
        """Random Walk Algorytm
        number_of_walk - number of walk (size of massive)
        massive = np based random massive 
        if element of massive >0.5 then massive will append counter number (default = 0) plus 
        random number from 0 to 2, else append counter minus random number 
        return list 
        """
        massive = np.random.random(self.number_of_walk) 
        walk_massive =[]
        counter=0
        for i in massive:
            if i>0.5:
                counter+=random.random()*3
            else:
                counter-=random.random()*3
            walk_massive.append(counter)
        return(walk_massive)
N =100 # Number of walks
x = Walk2d_massive(N).random_walk_algorytm() # x location
y = Walk2d_massive(N).random_walk_algorytm() # y location
z = Walk2d_massive(N).random_walk_algorytm() # z location
#loop for generation of ico sphere primitives
#radius is random from 0 to 2 
for i in range(N):
    #bpy.ops.mesh.primitive_ico_sphere_add(radius=random.random()*2, location=(x[i], y[i], z[i]))
    bpy.ops.object.metaball_add(radius=random.random()*4,location=(x[i], y[i], z[i]))      

#instead metaball you can generate also ico_sphere


    