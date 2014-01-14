#!/usr/bin/env python

import uuid

class Camera(object):
	def capture(self):
		image = image #capture an image from raspicam
		return image
	def save(self, image, path = None):
		path = path or ""
		imageId = str(uuid.uuid4())
		with open(path + imageId+'.png', 'wb') as f:
			f.write(image)
		return imageId

cam = Camera()
image = cam.capture()
cam.save(image)
print imageId
#do something with pic