# Import libraries
import threading
import socketserver
import socket
import cv2
import numpy as np
import math

# Config vars
server_ip = '192.168.1.235'
server_port = 8000
image_fps = 24 

# Class to handle the jpeg video stream received from client
class VideoStreamHandler(socketserver.StreamRequestHandler):
 
    def handle(self):
 
        stream_bytes = b
