import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy as np

options = {
    'model' : 'cfg/yolo.cfg',
    'load' : 'bin/yolo.weights',
    'threshold' : 0.3,
}

tfnet = TFNet(options)

img = cv2.imread('sample_img/dog_example.jpg',cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = tfnet.return_predict(img)

colors = [tuple(255*np.random.rand(3)) for _ in range(10)]
for color , result in zip(colors,results):
    tl = (result['topleft']['x'], result['topleft']['y'])
    br = (result['bottomright']['x'], result['bottomright']['y'])
    label = result['label']

    img = cv2.rectangle(img, tl, br, color, 7)
    img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX,1 ,(0,0,0), 2)
    print(cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX,1 ,(0,0,0), 2))

plt.imshow(img)
plt.show()
