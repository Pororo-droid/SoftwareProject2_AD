from darkflow.net.build import TFNet
import cv2

options = {
    'model' : 'cfg/yolo.cfg',
    'load' : 'bin/yolo.weights',
    'threshold' : 0.1
}

tfnet = TFNet(options)

imgcv = cv2.imread('./sample_img/sample_dog.jpg')
result = tfnet.return_predict(imgcv)

max_confidence = 0
result_label = ''
for i in range(len(result)):
    if result[i]['confidence'] > max_confidence:
        max_confidence = result[i]['confidence']
        result_label = result[i]['label']
print(result_label)