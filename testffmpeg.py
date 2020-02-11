import io
import os
import sys

def reencodefile(inname,outname):
	command = "ffmpeg -i {inname} -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M {outname}".format(inname=inname, outname=outname)
	try:
		os.system(command)
		print("reencode the video file succuessfully")
	except:
		print("failed to reencode")

	





try:
	inputname=sys.argv[1]
except:
	print("You should choose a input file!")
try:
	outputname=sys.argv[2]
except:
	print("You should gave a name to the output file!")
reencodefile(inputname,outputname)
