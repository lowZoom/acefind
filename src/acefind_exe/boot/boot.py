# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import acefind
from .arg_reader import CmdArgReader

class Boot(object):
	'''
	该类负责总控程序的启动逻辑
	'''
	def __init__(self,
		arg_reader=CmdArgReader(),
	):
		self._arg_reader = arg_reader
	
	def boot(self):
		argv = self._arg_reader.load_arg()
		
		print(acefind.__name__, acefind.__version__)
		print(argv)
	
