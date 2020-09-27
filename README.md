# Counting-Cars-in-Real-Time

This project uses OpenVINO and centroid tracking algorithm to count cars in Real Time


1. Go to installed location of OpenVINO and find the bin folder
2. Run the command setupvars.bat in the command prompt, which will initilaize the OpenVINO environment
3. Go to the project location and run the command: python cars_count.py -v test_video.mp4 -b ./FP32/vehicle-detection-adas-0002.bin -x ./FP32/vehicle-detection-adas-0002.xml
