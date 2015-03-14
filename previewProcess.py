#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-14 13:25:06
# @Author  : Black_Horse (heqingquan_tim@163.com)
# @Link    : http://no.com
# @Version : $Id$

import os
import os.path
import sys
import Image
from Image import EXTENT
import re

basePath = "E:/mycode/beauty"
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
		break
	return loc

def getMatrixImage(img):
	'''
	cut the top and the right
	'''
	w,h = img.size
	#print w,h
	if w>h:
		mimg = img.crop((0,w-h,h,h))
	else:
		mimg = img.crop((0,0,w,w))
	#mimg.show()
	return mimg
if __name__ == "__main__":
	loc = getFile(basePath)
	for f in loc:
		getMatrixImage(Image.open(os.path.join(basePath,f))).resize((35,35)).save(os.path.join(newPath,"new_"+str(f)),"jpeg")