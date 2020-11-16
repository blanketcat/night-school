#!/usr/bin/env python3


class Vertex(object):
	def __init__(self, name, data=None):
		self.name = name
		self.data = data


class Edge(tuple):
	def __init__(self, )