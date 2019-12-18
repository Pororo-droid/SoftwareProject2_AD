import random
def getImages():
    images = [
        "./images/guess/개미.png",'개미', "./images/guess/골목식당.png" ,'골목식당',
        "./images/guess/남녀노소.png",'남녀노소' ,"./images/guess/라이벌.png",'라이벌',
        "./images/guess/모자이크.png",'모자이크', "./images/guess/변화.png",'변화',
        "./images/guess/설거지.png",'설거지', "./images/guess/시어머니.png",'시어머니',
        "./images/guess/신사임당.png",'신사임당',"./images/guess/육군.png",'육군'
    ]
    ret_Images= []
    ret_Answers = []
    for i in range(5):
        idx = random.randrange(len(images)//2)
        ret_Images.append(images[idx*2])
        ret_Answers.append(images[idx*2+1])
        del images[idx*2]
        del images[idx*2]
    return ret_Images,ret_Answers

