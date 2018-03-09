###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr2
#Good Luck

from random import uniform
import time

class Plane():
	def __init__(self, orientation):
		self.orientation = orientation
		self.prev_orientation = 0

	def tilt(self, tilt):
		self.prev_orientation = self.orientation
		self.orientation += tilt

	def get_orientation(self):
		return self.orientation

	def correct(self):
		if(self.orientation < 0):
			self.orientation += (self.prev_orientation - self.orientation) * 2
		if(self.orientation > 0):
			self.orientation -= (self.prev_orientation - self.orientation) * 2

plane = Plane(0)

while True:
	pass
	print("angle: " + str(plane.get_orientation()))
	tilt = uniform(-2, 2)

	plane.tilt(tilt)
	time.sleep(1)



