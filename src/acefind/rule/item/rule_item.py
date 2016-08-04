# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

class RuleItem(object):
	'''
	该类表示一条匹配规则
	'''
	def __init__(self, rule_str):
		self._rule_str = rule_str
	
