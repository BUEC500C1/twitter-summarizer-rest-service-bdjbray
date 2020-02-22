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

`python twitter.py the_username_of_the_user the_location_of_the_background`

`the_username_of_the_user:`

Could be any user that you want to choose,should be their twitter username,not their real name.

Example:KingJames Example2:BarackObama

`the_location_of_the_background:`

The directory of the background paper that you want to choose.

I have provided one inside the main_exercise file.

Example: /Users/brayb/video-bdjbray/main_exercise/background.PNG


# Result and Notice

After the python command, if your see the below notice, pleace type y and press ENTER.

Because the program is splicing different images to a video.

![image](https://github.com/BUEC500C1/video-bdjbray/blob/master/imgs/notice.png)



















