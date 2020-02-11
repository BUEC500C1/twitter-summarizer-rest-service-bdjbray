# video-bdjbray
video-bdjbray created by GitHub Classroom

**Details of HW4:**
***
**Task1**

Estimate the processing power need to execute such operations on your computer

Estimate the maximum number of such operations that can run on your system

**Task2**

Design a module that can queue and process videos and notify the caller when the videos are ready

Implement the module

Include tracking interface to show how many processes are going on and success of each

**Main Exercise:** 

Using the twitter feed, construct a daily video summarizing a twitter handle day

Convert text into an image in a frame

Do a sequence of all texts and images in chronological order

Display each video frame for 3 seconds


**Solutions top the homework**
***

**Set up environment**
Download FFmpeg

Try to use command to re encode the video

convert mov to mp4  

`ffmpeg -i test.mov test.mp4`  

reencode video 720p at 2Mbps and 30fps

`ffmpeg -i test.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M output.mp4`

reencode video 480p at 1Mbps and 30fps

`ffmpeg -i input.mp4 -c:a copy -c:v copy -r 30 -s hd480 -b:v 1M output.mp4`












