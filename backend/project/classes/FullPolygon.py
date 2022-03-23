#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 12:25:39 2022

@author: anthonymac
"""

from functools import cmp_to_key
from time import perf_counter


# A class used to store the x and y coordinates of points.  Could be replaced with our point class but we dont need most of what our point class has for this operation.
class Point:
	def __init__(self, x = None, y = None):
		self.x = x
		self.y = y


class Polygon:
	def __init__(self, points):
		self.points = self.sortPoints(points)
		self.starting_point = self.points[0] #this will be the west most point of the polygon.
		self.number_of_points = len(self.points)
        
	def sortPoints(self, points): #sorts points from west to east.
		sorted_points = []
		for point in points:
			sorted_points.append(Point(point[0], point[1]))
			self.number_of_points = len(points)
		sorted_points.sort(key=lambda p : p.y)
		return sorted_points
		
	def nextToTop(self, S):
		return S[-2]

	def distSq(self, p1, p2):
		return ((p1.x - p2.x) * (p1.x - p2.x) +
				(p1.y - p2.y) * (p1.y - p2.y))
    
	def orientation(self, p, q, r):
		val = ((q.y - p.y) * (r.x - q.x) -
			(q.x - p.x) * (r.y - q.y))
		if val == 0:
			return 0 # collinear
		elif val > 0:
			return 1 # clock wise
		else:
			return 2 # counterclock wise
	
	#compares orientation of 2 points
	def compare(self, p1, p2): 
		orientation = self.orientation(self.starting_point, p1, p2)
		if orientation == 0:
			if self.distSq(self.starting_point, p2) >= self.distSq(self.starting_point, p1):
				return -1
			else:
				return 1
		else:
			if orientation == 2:
				return -1
			else:
				return 1
            
    #returns an array of points that make up the convex hull in order to make up a polygon.
	def convexHull(self):
		convexHull_array = [] #container for the points of the convex hull, in order for polygon.
		n = self.number_of_points
		points = self.points

		# Find the bottommost point.  This serves as the start for the scan
		ymin = points[0].y
		min = 0
		for i in range(1, n):
			y = points[i].y
			if ((y < ymin) or
				(ymin == y and points[i].x < points[min].x)):
				ymin = points[i].y
				min = i

		# Place the bottom-most point at first position
		points[0], points[min] = points[min], points[0]

		# Sort n-1 points with respect to the first point.
		# A point p1 comes before p2 in sorted output if p2
		# has larger polar angle (in counterclockwise
		# direction) than p1

		points = sorted(points, key=cmp_to_key(self.compare)) #second sort.

		# If two or more points make same angle with starting point,
		# Remove all but the one that is farthest from starting point
		# Remember that, in above sorting, our criteria was
		# to keep the farthest point at the end when more than
		# one points have same angle.
		m = 1 # Initialize size of modified array
		for i in range(1, n):

			# Keep removing i while angle of i and i+1 is same
			# with respect to starting point
			while ((i < n - 1) and
			(self.orientation(self.starting_point, points[i], points[i + 1]) == 0)):
				i += 1

			points[m] = points[i]
			m += 1 # Update size of modified array

		# If modified array of points has less than 3 points,
		# convex hull is not possible
		if m < 3:
			return

		# Create an empty list and push first three points to it.  This list is treated like a stack.  
		S = []
		S.append(points[0])
		S.append(points[1])
		S.append(points[2])

		# Process remaining n-3 points
		for i in range(3, m):

			# Keep removing top while the angle formed by
			# points next-to-top, top, and points[i] makes
			# a non-left turn
			while ((len(S) > 1) and
			(self.orientation(self.nextToTop(S), S[-1], points[i]) != 2)):
				S.pop()
			S.append(points[i])

		#pop items from stack and append to array to get points in the order needed for polygon.
		while S:
			p = S[-1]
			item = (p.x, p.y)
			convexHull_array.append(item)
			S.pop()
		
		return convexHull_array
            



