import io
import os
import sys


def addtext(inputname,outputname):
	cmd="ffmpeg -i {inputname} -vf drawtext=text='Test Text':fontcolor=black:fontsize=75:x=1002:y=100: {outputname}".format(inputname=inputname,outputname=outputname)
	os.system(cmd)

try:
	inputname=sys.argv[1]
except:
	print("You should choose a input file!")
try:
	outputname=sys.argv[2]
except:
	print("You should gave a name to the output file!")
addtext(inputname,outputname)