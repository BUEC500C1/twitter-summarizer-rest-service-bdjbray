# video-bdjbray
video-bdjbray created by GitHub Classroom

# Details of HW4:

### Task1

Estimate the processing power need to execute such operations on your computer

Estimate the maximum number of such operations that can run on your system

### Task2

Design a module that can queue and process videos and notify the caller when the videos are ready

Implement the module

Include tracking interface to show how many processes are going on and success of each

### Main Exercise

Using the twitter feed, construct a daily video summarizing a twitter handle day

Convert text into an image in a frame

Do a sequence of all texts and images in chronological order

Display each video frame for 3 seconds
<br />
<br />
# Solutions to the homework


### Set up environment

Download FFmpeg

Try to use command to re encode the video

convert mov to mp4  

`ffmpeg -i test.mov test.mp4`  

reencode video 720p at 2Mbps and 30fps

`ffmpeg -i test.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M output.mp4`

reencode video 480p at 1Mbps and 30fps

`ffmpeg -i test.mp4 -c:a copy -c:v copy -r 30 -s hd480 -b:v 1M output.mp4`

### TASK1

We can use `top` command our `iostat` command to check the CPU usage.

For my test, it takes 15.7% of my CPU, and my computer is quad-core.

So theoretically my computer can run 25 same operations in the same time.

### TASK2

A simple python code to for users to re-encode videos at 720p at 2Mbps and 30fps.

User should download FFmpeg first.

Run the program with command "python testffmpeg.py filename1 filename2".

filename1 is the name of the file you want to encode.

filename2 is the output file name you want.

### MAIN EXERCISE

Retrieve the tweets of a targeted user, and convert the text into a frame.

Play the video, each frame will be showed for 3 seconds.


# Setup

1,Use the below command line to download my repo:

`git clone https://github.com/BUEC500C1/video-bdjbray.git`

2,Use the below commad line to download the required files:

`pip3 install -r requirements.txt`

3,Replace the key in the file named twitter_credentials.py with your own key:


4,Use the below command line to run the program:

`python twitter.py the_username_of_the_user`

`the_username_of_the_user:`

Could be any user that you want to choose,should be their twitter username,not their real name.

Example:KingJames Example2:BarackObama

5,the six recent tweets of the selected user will be spliced into a video, each video frame will be displayed for three seconds.


# Result 


You can choose any user you want one at a time, the picture below is a result after retrieving tweets of three users.


![image](https://github.com/BUEC500C1/video-bdjbray/blob/master/imgs/result.png)


# Queue System

The program for queue system is in the main exercise file, named myQueueSystem.py

It will collect tweets and transfer to video for all the user's that in the name_list.

You will be informed which process is now going on, which process just finished and etc.

To run the program:

`python myQueueSystem.py`

You may change the users in the name_list to whoever you want. 

### Result

Some demos for the notices:

![image](https://github.com/BUEC500C1/video-bdjbray/blob/master/imgs/queueResult1.png)

![image](https://github.com/BUEC500C1/video-bdjbray/blob/master/imgs/queueResult2.png)


### Notice

If you see the notice below, please type y and press ENTER


![image](https://github.com/BUEC500C1/video-bdjbray/blob/master/imgs/notice.png)


















