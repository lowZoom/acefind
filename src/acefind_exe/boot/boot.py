# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import sys
import acefind

SYS_ENC = sys.getfilesystemencoding()

class Boot(object):
	'''
	该类负责总控程序的启动逻辑
	'''
	def __init__(self,
		sys_enc=SYS_ENC,
	):
		self._sys_enc = sys_enc
	
	def boot(self):
		win_path = lambda p:p.decode('utf-8').encode(SYS_ENC)
		argv = [win_path('.')]
		
		# 如果外部有参数传进来，则使用外部参数
		# 否则使用默认固定参数，方便测试
		if len(sys.argv) > 1:
			argv = sys.argv[1:]
		
		print(acefind.__name__, acefind.__version__)
		print(argv)
	
