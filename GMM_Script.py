import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat # loading data from matlab
from mpl_toolkits.mplot3d import Axes3D

import os
import pbdlib as pbd
import pbdlib.plot 
from pbdlib.utils.jupyter_utils import *
np.set_printoptions(precision=2)


########################################################################
##################CHANGE VALEUES HERE###################################
########################################################################
num_traj = 10

nb_states = 4  # choose the number of states in HMM or clusters in GMM

delt = .01

num_traj_points = 300
########################################################################
########################################################################


letter_in = 'traj_kinova' # INPUT LETTER: choose a letter in the alphabet

#datapath = os.path.dirname(pbd.__file__) + '/data/RobotData/'

#data_in = loadmat(datapath + '%s.mat' % letter_in)
data_in = loadmat('%s.mat' % letter_in)

demos_in = [d['pos'][0][0].T for d in data_in['posdemos'][0]] # cleaning matlab data
demos_out = [d['vel'][0][0].T for d in data_in['veldemos'][0]] # cleaning matlab data

demos = [np.concatenate([d_in, d_out], axis=1) 
         for d_in, d_out in zip(demos_in, demos_out)]

fig, ax = plt.subplots(ncols=3)  
fig.set_size_inches(18., 8.5)
plt.tight_layout()

[ax[i].set_title(s) for i, s in enumerate(['input', 'output'])]

ax = fig.add_subplot(1,2,1, projection = '3d')
A = np.arange(num_traj_points)
B = np.arange(num_traj)
for l in B:
    x = np.array(demos_in[l])
    xp = x[:,0]
    yp = x[:,1]
    zp = x[:,2]  
    
    ax.plot3D(xp,yp,zp, linewidth = 2, antialiased=True)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

ax = fig.add_subplot(1,2,2, projection = '3d')
B = np.arange(num_traj)
for l in B:
    x = np.array(demos_out[l])
    xp = x[:,0]
    yp = x[:,1]
    zp = x[:,2]  

    ax.plot3D(xp,yp,zp, linewidth = 2, antialiased=True)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')


np.stack(demos).shape




# creating models
gmm = pbd.GMM(nb_states=nb_states)
hmm = pbd.HMM(nb_states=nb_states)
hsmm = pbd.HSMM(nb_states=nb_states)

# initializing model by splitting the demonstrations in k bins
[model.init_hmm_kbins(demos) for model in [gmm, hmm, hsmm]] 

# EM to train model
gmm.em(np.concatenate(demos), reg=1e-8) 
hmm.em(np.stack(demos), reg=1e-8) 
hsmm.em(demos, reg=1e-6) 

#THIS IS THE SAVED SIGMA AND MU VALUES
# savedsigma = gmm.sigma
# savedmu = gmm.mu

savedsigma = gmm.sigma
savedmu = gmm.mu 

file1 = open("/home/hulk/Documents/waypoints/f1.txt","w") 

L = np.array2string(savedmu, precision=4, separator=',', suppress_small=True)  
file1.writelines(L)
file1.write("\n")
L = np.array2string(savedsigma, precision=4, separator=',', suppress_small=True)  
file1.writelines(L)
file1.write("\n")




from numpy import array

y = np.array([.5,.1,.1])
y.shape = (1,3)

mu_est_gmm, sigma_est_gmm = gmm.condition(
    y, dim_in=slice(0, 3), dim_out=slice(3, 6))
# mu_est_hmm, sigma_est_hmm = hmm.condition(
#     y, dim_in=slice(0, 3), dim_out=slice(3, 6))
# mu_est_hsmm, sigma_est_hsmm = hsmm.condition(
#     y, dim_in=slice(0, 3), dim_out=slice(3, 6))








fig.set_size_inches(25, 15)
file1 = open("/home/hulk/Documents/waypoints/f1.txt","w") 
A = np.arange(num_traj_points)


y = array([.45,-.2,.4])
y.shape = (1,3)

#CAN CHANGE DELTA VALUE HERE
delt = .1
pos = array([0,0,0])
pos.shape = (1,3)
pos = y + mu_est_gmm*delt

#3D VERSION
#CAN CHANGE THE NUMBER OF ITERATIONS HERE
for j in A:
    temp = pos[j]
    temp.shape = (1,3) 
    mu_est_gmm, sigma_est_gmm = gmm.condition(temp, dim_in=slice(0, 3), dim_out=slice(3, 6))
    newpos = temp + mu_est_gmm*delt
    newpos.shape = (1,3)
    finalresult = np.concatenate((pos,newpos),axis=0)
    pos = finalresult

fig, ax = plt.subplots(ncols=2)
fig.set_size_inches(20., 20)
ax = fig.add_subplot(1,1,1, projection = '3d')

file2 = open("/home/hulk/Documents/waypoints/f2.txt","w") 

C = np.arange(num_traj)
for m in C:
    x = np.array(demos_in[m])
    xp = x[:,0]
    yp = x[:,1]
    zp = x[:,2]  
    ax.plot3D(xp,yp,zp, linewidth = 2, antialiased=True)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

ax.plot3D(pos[:,0],pos[:,1],pos[:,2],linewidth = 5, color='black')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


L = np.array2string(pos, precision=4, separator=',', suppress_small=True)  
file2.writelines(L)
file2.write("\n\n\n")

y = array([.2,0.0,.3])
y.shape = (1,3)
mu_est_gmm, sigma_est_gmm = gmm.condition(
    y, dim_in=slice(0, 3), dim_out=slice(3, 6))

pos = array([0,0,0])
pos.shape = (1,3)
pos = y + mu_est_gmm*delt

for j in A:
    temp = pos[j]
    temp.shape = (1,3) 
    mu_est_gmm, sigma_est_gmm = gmm.condition(temp, dim_in=slice(0, 3), dim_out=slice(3, 6))
    newpos = temp + mu_est_gmm*delt
    newpos.shape = (1,3)
    finalresult = np.concatenate((pos,newpos),axis=0)
    pos = finalresult

ax.plot3D(pos[:,0],pos[:,1],pos[:,2],linewidth = 5, color='green')


L = np.array2string(pos, precision=4, separator=',', suppress_small=True)  
file2.writelines(L)
file2.write("\n\n\n")


y = array([.5,.25,.25])
y.shape = (1,3)
mu_est_gmm, sigma_est_gmm = gmm.condition(
    y, dim_in=slice(0, 3), dim_out=slice(3, 6))

pos = array([0,0,0])
pos.shape = (1,3)
pos = y + mu_est_gmm*delt

y = array([.4,-.3,.3])
y.shape = (1,3)
mu_est_gmm, sigma_est_gmm = gmm.condition(
    y, dim_in=slice(0, 3), dim_out=slice(3, 6))

pos = array([0,0,0])
pos.shape = (1,3)
pos = y + mu_est_gmm*delt

for j in A:
    temp = pos[j]
    temp.shape = (1,3) 
    mu_est_gmm, sigma_est_gmm = gmm.condition(temp, dim_in=slice(0, 3), dim_out=slice(3, 6))
    newpos = temp + mu_est_gmm*delt
    newpos.shape = (1,3)
    finalresult = np.concatenate((pos,newpos),axis=0)
    pos = finalresult

ax.plot3D(pos[:,0],pos[:,1],pos[:,2],linewidth = 5, color='yellow')

plt.show()


L = np.array2string(pos, precision=4, separator=',', suppress_small=True)  
file2.writelines(L)
file2.write("\n\n\n")

file1.close() #to change file access modes 
file2.close() #to change file access modes 



