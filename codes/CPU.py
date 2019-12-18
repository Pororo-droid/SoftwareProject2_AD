from darkflow.net.build import TFNet
import cv2

def start():
    options = {
        'model' : 'cfg/yolo.cfg',
        'load' : 'bin/yolo.weights',
        'threshold' : 0.1
    }

    tfnet = TFNet(options)
    print(2)
    imgcv = cv2.imread('./images/test.png')
    result = tfnet.return_predict(imgcv)
    print(1)
    max_confidence = 0
    result_label = ''
    for i in range(len(result)):
        if result[i]['confidence'] > max_confidence:
            max_confidence = result[i]['confidence']
            result_label = result[i]['label']
    if(result_label == ''):
        print("?????")
    else:
        print(result_label)
    return result_label