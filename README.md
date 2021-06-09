# Counting Cars in Real Time

This project uses OpenVINO and centroid tracking algorithm to count cars in Real Time
Video Demo


[![Video_Demo](https://img.youtube.com/vi/LXKNNdLjTJ0/0.jpg)](https://www.youtube.com/watch?v=LXKNNdLjTJ0)


## Requirements:

- OpenCV
- OpenVINO

## Steps to run the program:

1. Go to installed location of OpenVINO and find the bin folder
2. Run the command `setupvars.bat` in the command prompt, which will initilaize the OpenVINO environment
3. Go to the project location and run the command: `python cars_count.py -v test_video.mp4 -b ./FP32/vehicle-detection-adas-0002.bin -x ./FP32/vehicle-detection-adas-0002.xml`


Note that the bin & xml files here are according to version 2019, which may not be compatible with your version of OpenVINO.
For more info, refer [this blog](https://www.hackster.io/computervisionpro/counting-cars-in-real-time-1937d7) that I wrote for this project.
