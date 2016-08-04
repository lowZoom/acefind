# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

class RuleSet(object):
	'''
	该类表示一次查找中会用到的所有匹配规则集合
	'''
	def __init__(self, rule_list):
		self._rule_list = rule_list
	
