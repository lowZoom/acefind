# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

class RuleSet(object):
	'''
	该类表示一次查找中会用到的所有匹配规则集合
	'''
	def __init__(self, item_list):
		self._item_list = item_list
	
