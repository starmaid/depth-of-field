# this will be similar to the regular stream example
# but i want to do a trick to get more depth resolution out of the RGB stream without going to 16bit, because i dont think it can do that


import pyrealsense2 as rs
import numpy as np
import cv2
import aiortc


PIPELINE_OUT = "appsrc ! ... ! tcpserversink host=127.0.0.1 port=5000"

video_in = cv2.VideoCapture(1, cv2.CAP_DSHOW)
video_in.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_in.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


video_out = cv2.VideoWriter(PIPELINE_OUT, cv2.CAP_GSTREAMER, 0,30,(640,480))

ls_1 = "appsrc ! videoconvert ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000"

ls_2 = 'appsrc name=source is-live=true block=true format=GST_FORMAT_TIME ' \
                             'caps=video/x-raw,format=BGR,width=640,height=480,framerate=30/1 ' \
                             '! videoconvert ! video/x-raw,format=I420 ' \
                             '! x264enc speed-preset=ultrafast tune=zerolatency ' \
                             '! rtph264pay config-interval=1 name=pay0 pt=96'

h264_shmsink = cv2.VideoWriter(ls_2,
     cv2.CAP_GSTREAMER, 0, float(30), (int(640), int(480)))


while True:
    okay, image = video_in.read()
    h264_shmsink.write(image)
    cv2.imshow("prev",image)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

