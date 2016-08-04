# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import sys
import acefind

SYS_ENC = sys.getfilesystemencoding()

class Boot(object):
	def __init__(self,
		sys_enc=SYS_ENC,
	):
		self._sys_enc = sys_enc
	
	def boot(self):
		win_path = lambda p:p.decode('utf-8').encode(SYS_ENC)
		argv = [win_path('.')]
		
		if len(sys.argv) > 1:
			argv = sys.argv[1:]
		
		print(acefind.__version__)
		print(argv)
	
