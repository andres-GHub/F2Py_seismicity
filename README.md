# F2Py_seismicity
## Generating/analyzing a synthetic catalog of earthquake events and model testing ##

Datalogy class project, Fall 2015
Code to import FORTRAN program and analyze ETAS model as well as a self-similar model
(see: J. Davidsen & M. Baiesi 2015 for the self similar model). The self similar model 
program is a modification of the ETAS model program

Currently unable to run the FORTRAN program from Python after
importing ETAS.so file. For now the program must be compiled and executed in FORTRAN in 
order to obtain the synthetic catalogue which we then read into Python for analysis

#######
Notes on the current FORTRAN code: The FORTRAN code used to generate the data for the 
ETAS model was written by Karen Felzer and Yu Gu, spring 2001, and modified
by A. Helmstetter 2002-2011. It can be obtained in the following website: 
www.corssa.org/software under the subsection "Seismicity modeling and forecasting:
short-term". 
In order for Python to read and execute the FORTRAN program, it must first be converted
to a '.so' format. The previous can be done by using the 'f2py' function in the 
command line (not in Python). Applying the 'f2py' function on the original code was 
not successful in creating an '.so' file. This conversion was latter accomplished by
changing the file extension name from its original '.f77' to '.f95' (and editing the 
initiation of comments in the code from 'c' --> '!'). After this edit, a '.so' and '.o'
were created which were then imported into Python. The main issue at the moment is that 
Python is unable to make a call for the '.so' program to run (the '.so' file does not
show any of the subroutines or name of the main program when queried through the 'dir(ETAS)'
function in Python). 
The parameters for the model at the moment need to be entered in a separate text file,
but this will be delegated to Python once the issue(s) with '.so' file are resolved.
As of now, I am unable to call the FORTRAN program directly in Python (it can be 
imported). It must first be compiled (I have used gfortran under the Geany IDE)
so that it produces an executable which can then be run from Python 
(see: subprocess.Popen() ... function below) to then produce the catalog

Note:
Code sections marked as:
           #########
           # XXXXXX
           #########
are parts of code that may be relevant for other uses or code which I'm currently
working on.
