## Generating/analyzing a synthetic catalog of earthquake events and model testing ##

# Datalogy class project, Fall 2015
# Code to import FORTRAN program and analyze ETAS model as well as a self-similar model
# (see: J. Davidsen & M. Baiesi 2015 for the self similar model). The self similar model 
# program is a modification of the ETAS model program

# Currently unable to run the FORTRAN program from Python after
# importing ETAS.so file. For now the program must be compiled and executed in FORTRAN in 
# order to obtain the synthetic catalogue which we then read into Python for analysis

#######
# Notes on the current FORTRAN code: The FORTRAN code used to generate the data for the 
# ETAS model was written by Karen Felzer and Yu Gu, spring 2001, and modified
# by A. Helmstetter 2002-2011. It can be obtained in the following website: 
# www.corssa.org/software under the subsection "Seismicity modeling and forecasting:
# short-term". 
# In order for Python to read and execute the FORTRAN program, it must first be converted
# to a '.so' format. The previous can be done by using the 'f2py' function in the 
# command line (not in Python). Applying the 'f2py' function on the original code was 
# not successful in creating an '.so' file. This conversion was latter accomplished by
# changing the file extension name from its original '.f77' to '.f95' (and editing the 
# initiation of comments in the code from 'c' --> '!'). After this edit, a '.so' and '.o'
# were created which were then imported into Python. The main issue at the moment is that 
# Python is unable to make a call for the '.so' program to run (the '.so' file does not
# show any of the subroutines or name of the main program when queried through the 'dir(ETAS)'
# function in Python). 
# The parameters for the model at the moment need to be entered in a separate text file,
# but this will be delegated to Python once the issue(s) with '.so' file are resolved.
# As of now, I am unable to call the FORTRAN program directly in Python (it can be 
# imported). It must first be compiled (I have used gfortran under the Geany IDE)
# so that it produces an executable which can then be run from Python 
# (see: subprocess.Popen() ... function below) to then produce the catalog

# Note:
# Code sections marked as:
#            #########
#            # XXXXXX
#            #########
# are parts of code that may be relevant for other uses or code which I'm currently
# working on.
############################################################################################
#     Copyright 2015 Andres Zambrano
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.

# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.

# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see <https://www.gnu.org/licenses/>.


import scipy
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import filecmp
import matplotlib
import matplotlib.cm as cm
#Run external program
import subprocess,time
#Read external file data
import csv


######################################
#Read/run files from another directory
#from os import path
######################################

#import sys, os, string
#Import into python the .so file
#import ETAS

#############################
#To change file path name
#import os
#############################

#########################################################################
###### A way to rename file EXTENSION/NAME of catalog output if necessary
#if os.path.isfile('ETAS.cat') == True:
#    os.rename('ETAS.cat','ETAS.txt')
#########################################################################


# Run executable file which is produced after compiling the FORTRAN ETAS source code (set to run 
# in the same directory as the current Python program). Need to give some time for the executable 
# to generate the catalog or else one obtains the following: "IndexError: list index out of range"
subprocess.Popen("./ETAS")
time.sleep(4.91)


#################################
#subprocess.Popen("./ETAS2/ETAS")
#time.sleep(4.91)
#################################


# Reading the output catalog generated from the FORTRAN code (same file as Python notebook)
# and creating an array for each parameter in the catalog based on the name in the '.cat'
# file.
with open('ETAS.cat', 'rt') as f:  

  reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
  
  #Skip first 3 lines of ETAS.cat output file
  next(reader)
  next(reader)
  next(reader)

  lineData = list()

  cols = next(reader)
  print(cols)

  for col in cols:
    # Create a list in lineData for each column of data.
    lineData.append(list())


  for line in reader:
    for i in xrange(0, len(lineData)):
    # Copy the data from the line into the correct columns.
      lineData[i].append(line[i])

  data = dict()

  for i in xrange(0, len(cols)):
    # Create each key in the dict with the data in its column.
    data[cols[i]] = lineData[i]
    

################################################
#filepathETAS2 = path.relpath('/ETAS2/ETAS.cat')
################################################

# Reading second synthetic catalog
with open('ETAS2.cat', 'rt') as f2:  

  reader2 = csv.reader(f2, delimiter=' ', skipinitialspace=True)
  
  #Skip first 3 lines of ETAS2.cat output file
  next(reader2)
  next(reader2)
  next(reader2)

  lineData2 = list()

  cols2 = next(reader2)
  print(cols2)

  for col2 in cols2:
    # Create a list in lineData2 for each column of data.
    lineData2.append(list())


  for line2 in reader2:
    for i in xrange(0, len(lineData2)):
    # Copy the data from the line into the correct columns.
      lineData2[i].append(line2[i])

  data2 = dict()

  for i in xrange(0, len(cols2)):
    # Create each key in the dict with the data in its column.
    data2[cols2[i]] = lineData2[i]



    
# Plotting time vs magnitude for all events in the catalog
plt.clf()
plt.plot(data['time'],data['mag'],'r-')
plt.title('Magnitude vs time plot, ETAS')
plt.axis([0,2001,0,6.2])
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

# Rename and transform string lyst into numbers(float) in order to manipulate data
# for visualizing in plots

mags=data['mag']
times=data['time']
xs=data['x']
ys=data['y']


######################
#def scatterxymags():
######################

    
mags=np.array(mags).astype(np.float)
times=np.array(times).astype(np.float)
xs=np.array(xs).astype(np.float)
ys=np.array(ys).astype(np.float)

mags2=data2['mag']
times2=data2['time']
xs2=data2['x']
ys2=data2['y']
    
mags2=np.array(mags2).astype(np.float)
times2=np.array(times2).astype(np.float)
xs2=np.array(xs2).astype(np.float)
ys2=np.array(ys2).astype(np.float)


# Function to reset data if its modified
def resetdata():
    global mags
    mags=data['mag']
    mags=np.array(mags).astype(np.float)
    return mags


# Find the maximum magnitude in order to use in the color function; want to divide
# by the largest possible value of magnitudes in a given catalog.

maxmag=max(mags)

color = [str(item/maxmag) for item in mags]
# Size of circle in scatter-plot will depend of magnitude of eartquake
siz = [40*mags[n] for n in range(len(mags))]

plt.clf()   
plt.scatter(xs, ys, s=siz, c=mags,alpha = 0.51, cmap=cm.Paired)
plt.title('2D position and magnitudes, ETAS')
plt.xlim(0,1000)
plt.ylim(0,1000)
plt.xlabel('x (Km)')
plt.ylabel('y (Km)')
plt.colorbar().ax.set_ylabel('Magnitude', rotation=270, labelpad = 17)
plt.show()

################    
#scatterxymags()
################

# Function to better visualize earthquakes of higher magnitude.
def WeighLargeMags():
    
    for i in range(0,len(mags)):
    
        if 0.0 <= mags[i] < 1.0:
        
            mags[i]=mags[i]/100.0
        
        if  1.0 <= mags[i] <= 2.0:
        
            mags[i]=mags[i]/100.0
        
        if  2.0 < mags[i] <= 3.0:
        
            mags[i]=mags[i]/100.0
        
        if 3.0 < mags[i] <= 4.0:
        
            mags[i]=mags[i]/100.0
        
        if 4.0 < mags[i] <= 4.01:
        
            mags[i]=mags[i]*1.0
    
        if mags[i] > 4.01:
        
            mags[i]=mags[i]*1.0
            
    #maxmag=max(mags)-5
    

    color = [str(item/maxmag) for item in mags]
    siz = [40*mags[n] for n in range(len(mags))]
    
    plt.clf()
    plt.scatter(xs, ys, s=siz, c=mags, alpha = 0.71, cmap=cm.gist_rainbow_r)
    plt.title ('2D position and weighted magnitude for mag > 4, ETAS')
    plt.xlim(0,1000)
    plt.ylim(0,1000)
    plt.xlabel('x (Km)')
    plt.ylabel('y (Km)')
    plt.colorbar().ax.set_ylabel('Magnitude', rotation=270, labelpad = 17)
    plt.show()
    
WeighLargeMags()
resetdata()

# Function to compare catalog magnitudes and do correlation analysis
def comparecatalogs():
    global mags, mags2
    # Converting arrays to list so that they can be manipulated
    mags=mags.tolist()
    mags2=mags2.tolist()
    # creating lists that are equal in length in order to compare
    # since the the catalogs are of the same order, removing a fraction
    # of the data should not have much impact on, say, the correlation 
    # in the case of the ETAS model since it is a Poisson process by
    # construction. This approximation and its validity would need to
    # be looked at more carefully for the self-similar model 
    if len(mags) > len(mags2):
        lenmaxmag = len(mags2)
        del mags[lenmaxmag:]
    if len(mags) <= len(mags2):
        lenmaxmag = len(mags)
        del mags2[lenmaxmag:]
    # Correlation between magnitudes between 2 different catalogs of 
    # the ETAS model should be close to 0 since the model is a Poisson
    # process by construction.
    corrmags = np.corrcoef(mags, mags2)[0, 1]
    print ''
    print 'Correlation between magnitudes of two catalogs:', corrmags
    
    # Scatter and histogram plot of magnitude data from two different ETAS catalogs
    plt.clf()
    plt.scatter(mags, mags2)
    plt.title ('Scatter Plot of magnitudes for 2 different catalogs, ETAS')
    plt.xlim(0,7)
    plt.ylim(0,7)
    plt.xlabel('Magnitude')
    plt.ylabel('Magnitude')
    plt.show()
    
    plt.clf()
    plt.hist2d(mags, mags2, bins=90)
    plt.title ('Histogram of magnitudes for 2 different catalogs, ETAS')
    plt.xlabel('Magnitude')
    plt.ylabel('Magnitude')
    plt.show()
    
corrmags = np.corrcoef(mags, mags)[0, 1]
print ''
print 'Correlation between magnitudes of same catalog:', corrmags
print ''
comparecatalogs()


##########################################################################
# using and modifying code from:
# http://matplotlib.org/api/pyplot_api.html

# make a little extra space between the subplots
plt.subplots_adjust(wspace=0.5)

dt = 0.01
t = times
nse1 = mags                 # white noise 1
nse2 = mags2                 # white noise 2
r = np.exp(-t/0.05)

cnse1 = np.convolve(nse1, r, mode='same')*dt   # colored noise 1
cnse2 = np.convolve(nse2, r, mode='same')*dt   # colored noise 2

# two signals with a coherent part and a random part
s1 = cnse1
s2 = cnse2

plt.subplot(211)
plt.plot(t, s1, 'b-', t, s2, 'g-')
plt.xlim(0, 1000)
plt.xlabel('time')
plt.ylabel('s1 and s2')
plt.grid(True)

plt.subplot(212)
cxy, f = plt.cohere(s1, s2, 256, 1./dt)
plt.ylabel('coherence')
plt.show()
##########################################################################
