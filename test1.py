#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-13 15:28:44
# @Author  : Black_Horse (heqingquan_tim@163.com)
# @Link    : http://no.com
# @Version : $Id$

import os
import Image
import os.path
import sys
import re

bathPath = "E:/mycode/beauty"
newPath = "E:/mycode/beauty/new"

def getFile(loc_url):
	'''
	Get the image of the loc_url,which is in the folder;
	'''
	loc = []
	pattern = re.compile(r".*\.[Jj][Pp][Ee][Gg]")
	for root,dirs,files in os.walk(loc_url):
		for f in files:
			# print f
			if pattern.match(f):
				loc.append(f)
	return loc

def resizeImage(in_url,out_url,size=(35,35)):
	'''
	Change the Image in in_url and save it in the out_url
	size if a 
	'''
	if os.path.exists(in_url):
		Image.open(in_url).resize((size)).save(out_url,'JPEG')

def Test(str1):
	print "hello"+str(str1)
if __name__=="__main__":
	Test("world")

# 	loc = getFile(bathPath)
# 	# img1 = Image.open(os.path.join(bathPath,loc[1]))
# 	# img1.show()
# 	for f in loc:
# 		resizeImage(os.path.join(bathPath,f),os.path.join(newPath,"new_"+str(f)),(35,35))

