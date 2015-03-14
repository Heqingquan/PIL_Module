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
import math
import random
from previewProcess import getFile
bathPath = "E:/mycode/beauty"
newPath = "E:/mycode/beauty/new"


def resizeImage(in_url,out_url,size=(35,35)):
	'''
	Change the Image in in_url and save it in the out_url
	size if a 
	'''
	if os.path.exists(in_url):
		Image.open(in_url).resize((size)).save(out_url,'JPEG')

def getMean(in_url):
	'''
	Get the mean RGB of the in_url Image
	'''
	R = []
	G = []
	B = []
	img = Image.open(in_url)
	imgdata = img.getdata()
	for pix in imgdata:
		if type(pix) is type(1):
			return None
		R.append(pix[0])
		G.append(pix[1])
		B.append(pix[2])
	R.sort()
	G.sort()
	B.sort()
	return int(math.sqrt((R[len(R)/2]**2+G[len(R)/2]**2+B[len(R)/2]**2)/3))

def SaveImageMean(fileList):
	'''
	save the list of the Image and the sequence
	'''
	colorlist = [[] for i in xrange(255)]
	for f in fileList:
		# print ("Get data from Image %s" %f)
		seq = getMean(os.path.join(newPath,f))
		if seq is not None:
			colorlist[seq].append(f)
		#colorlist[seq].append(f)
	return colorlist

def getProbList(fileList,pix):
	'''
	get file list which data is nearly equal to pix
	'''
	if len(fileList[pix]) is not 0:
		return fileList[pix]
	else:
		for i in xrange(100):
			if pix+i <254:
				if len(fileList[pix+i]) != 0:
					return fileList[pix+i]
			if pix-i >=0:
				if len(fileList[pix-i]) != 0:
					return fileList[pix-i]

def getrandomfile(namelist):
	return random.choice(namelist)

def createImage(in_file):
	'''
	use the file in the demo_list create the new Image;
	'''
	x0 = 0
	x1 = 35
	y0 = 0
	y1 = 35
	count = 0
	img_in = Image.open(in_file)
	w,h = img_in.size
	#print w
	newImg = Image.new("RGB",(w*35,h*35))
	loc = getFile(newPath)
	list1 = SaveImageMean(loc)
	for pix in img_in.getdata():
		flist = getProbList(list1,pix)
		f = getrandomfile(flist)
		#print ("paste file %s" %f)
		newImg.paste(Image.open(os.path.join(newPath,f)),(x0,y0,x1,y1))
		count +=1
		x0 =(count%35)*35
		x1 = x0+35
		y0 = count//35*35
		y1 = y0+35
	return newImg




def processDemo(url):
	img = Image.open(url).convert("L")
	w,h = img.size
	img2 = img.resize((35,int(h*35/w)))
	img2.save("img2.jpeg","jpeg")
if __name__=="__main__":
	#print len([])
	mimg = createImage("img2.jpeg")
	baseimage = Image.open('demo2.png').resize(mimg.size)
	newimg = Image.blend(mimg,baseimage,0.2).save("newimg.jpeg","jpeg")
	#processDemo("demo2.png")
	 # img3 = Image.open("img2.jpeg")
	 # box = (100,100,img3.size[0]+100,img3.size[1]+100)
	 # img4 = Image.open("demo.jpeg")
	 # img4.paste(img3,box)
	 # img4.show()

	#loc = getFile(newPath)
	# #print loc
	# list1 = SaveImageMean(loc)
	# print list1
	#img1 = Image.open(os.path.join(bathPath,loc[1]))
	#print getMean(os.path.join(bathPath,loc[1]))
	#Image.open(os.path.join(bathPath,loc[1])).convert("L").save("demo.jpeg","JPEG")
	#img2 = Image.open("demo.JPEG")
	#print list(img2.getdata())[1]

	
	# img1.show()
	# for f in loc:
	# 	resizeImage(os.path.join(bathPath,f),os.path.join(newPath,"new_"+str(f)),(35,35))

