#!/usr/local/env python
# *-* coding:utf-8 *-*
#author:wuling
#date:2020/1/14

"""
解析文件，提取数据，构建数据库（mysql）
"""

import os
import math
from pprint import pprint
from collections import OrderedDict

current_path = os.path.dirname(os.path.abspath(__name__))

def preProcess(filepath):

	with open(filepath) as rf:

		key_vallength = OrderedDict()

		n = 0

		for line in rf:
			
			data = [d.strip() for d in line.split('\t')]

			if n == 0:
				head = data
				pprint(head)
				# pprint(len(head))
			else:
				unit = OrderedDict(zip(head,data))

				for key,val in unit.items():
					if key not in key_vallength:
						key_vallength[key]=0
					key_vallength[key] = max(len(val),key_vallength[key])

			n += 1

		# pprint(key_vallength)

		for key,val in key_vallength.items():

			key_type = "VARCHAR"

			val_length = len(str(val))

			length = 10**val_length

			if length >65535 :
				key_type = "TEXT"

			# print key + ' {}({}),'.format(key_type,length)
			# print (key + ' = ' + "db.Column(db.String({}))").format(length)
			# print("self." + key + " = " +  key)
			print key + ',',

def main():
	filepath = os.path.join(current_path,"data","original","SRP027383_known_fusion_event.txt")
	preProcess(filepath)

if __name__ == "__main__":
	main()