#!/bin/bash

echo "init video stream..."
raspivid -o - -t 0 -fps 25 -w 640 -h 480 -n | cvlc -v stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

# 	Params:
#	-t   	=  	start time (0 = now)
#	-fps	=	frame rate
#	-w,-h	= 	image  width,height

# 	NOTE: it will stream at whatever the wifi/ethernet channel can handle, likely lower fps than parameter states
