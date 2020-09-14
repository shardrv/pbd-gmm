# Gaussian Mixture Model 
Using Sylvian Calinon's pbdlib repo to recreate GMM/HMM for Robot trajectories 

*The repository contains the procedure to recreate the GMM/HMM/HSMM models demonstrated in Sylvian Calinon's pbdlib-python repository [Link: https://gitlab.idiap.ch/rli/pbdlib-python.git] in order to train the robot trajectories for the aim of achieving LfD learning from demonstrations.*


## Procedure

### Create Folder

Clone the repository
```
git clone https://gitlab.idiap.ch/rli/pbdlib-python.git
```

### Setup Environment

Within the *pbdlin-python* folder setup the python 2.7 virtual environment using:

```
virtualenv -p /usr/bin/python2,7 py27venv
```

Enter the virtualenv using:

```
source py27venv/bin/activate
```

Install pbdlib 

```
pip install -e .
```

Now copy the jupyter notebook ipynb file in this repository into the *notebooks* folder and open the jupyter notebook using 

```
jupyter notebook notebooks/
```

### Trajectories in the RobotData Folder

You will need the *new_traj.mat* matlab file in the RobotData folder within the */pbdlib/data/RobootData* folder for this code to work.

Now all your trajectories are read and displayed in the jupyter file.


*This work is a combined effort of the Computer Vision and Robotics Laborartory at the University of Alberta under the supervision of Dr. Martin Jagersand.*


