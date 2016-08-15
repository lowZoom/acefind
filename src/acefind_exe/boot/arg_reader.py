# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import sys

SYS_ENC = sys.getfilesystemencoding()

class CmdArgReader(object):
	'''
	该类负责读取并解析命令行传进来的参数
	'''
	def load_arg(self):
		win_path = lambda p:p.decode('utf-8').encode(SYS_ENC)
		argv = [win_path('.')]
		
		# 如果外部有参数传进来，则使用外部参数
		# 否则使用默认固定参数，方便测试
		if len(sys.argv) > 1:
			argv = sys.argv[1:]
		
		return argv
	
	def read_target_path(self, arg_list):
		return u''
	
	def read_rule_input(self, arg_list):
		return u''
	
