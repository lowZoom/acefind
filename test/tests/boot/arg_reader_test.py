# -*- coding: utf-8 -*-
from __future__ import division, print_function
from unittest import TestCase
from hamcrest import assert_that, equal_to
#from mock import MagicMock
from . import CmdArgReader

class CmdArgReaderTest(TestCase):
	''''''
	def setUp(self):
		self.reader = CmdArgReader()
	
	def test_read_target_path(self):
		# Arrange
		reader = self.reader
		arg = [r'd:\target_dir', 'other_arg']
		
		# Act
		result = reader.read_target_path(arg)
		
		# Assert
		assert_that(result, equal_to(r'd:\target_dir'))
	
