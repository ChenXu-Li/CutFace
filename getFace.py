import cv2

#face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
flag = cap.isOpened()
sampleNum=0
Id=3
camera_flag=False

while (flag):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
      gray,
      scaleFactor = 1.15,#缩放比
      minNeighbors = 10,#敏感度
      minSize = (5,5),
      #flags = cv2.HAAR_SCALE_IMAGE
    )
    cv2.imshow("Capture_Paizhao", frame)
    print ("发现{0}个人脸!".format(len(faces)))
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
        cv2.imshow("Capture_Paizhao", frame)
    if(camera_flag):
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow("Capture_Paizhao", frame)
            k1 = cv2.waitKey(0) & 0xFF
            if k1 == ord('s'):
                sampleNum = sampleNum + 1
                cv2.imwrite("./dataSet/User." + str(Id) + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])  #
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imshow("Capture_Paizhao", frame)
                cv2.waitKey(0)
                continue
            elif k1==ord('n'):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
          
            
        camera_flag=False
    
    k = cv2.waitKey(33) & 0xFF
    if k == ord('q'): 
        break
    elif k == ord('c'):
        camera_flag=True
cap.release() # 释放摄像头
cv2.destroyAllWindows()