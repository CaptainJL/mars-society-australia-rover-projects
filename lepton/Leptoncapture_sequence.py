import numpy as np
import cv2
import time
from pylepton import Lepton





with Lepton() as l:
	i=0
	while i<10:	# save 10 images
		a,_ = l.capture()  
		cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
		np.right_shift(a, 8, a)
		saveloc = str(i) + ".jpg"
		cv2.imwrite(saveloc, np.uint8(a)) 
		time.sleep(0.5)
		i=i+1