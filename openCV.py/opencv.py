import cv2
# img=cv2.imread("001.jpg") #讀取圖片附檔案名
# img=cv2.resize(img, (0, 0), fx=0.5, fy=0.5) #設置圖片大小，則fx=, fy= 是倍數的呈現
# cv2.imshow("img", img)
# cv2.waitKey(0)
# ///////////////////////////////////////////////////////////////
 
# import numpy as np
# import random  #導入隨機變數
# img=np.empty((300, 300, 3),np.uint8) #uint8,因2進至為2^8,另外(300, 300, 3)這一部份為長寬各300格方塊，3則因RBG有三層顏色所出來的

# for row in range(300): #用for迴圈給img(陣列)裡面的值給予RGB顏色
#     for col in range(300):
#         img[row][col] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)] #隨機變數random.randint(0, 255),0~255之間

# cv2.imshow("img", img)
# cv2.waitKey(0)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#抓出圖片中的輪廓
# img=cv2.imread("pic.png")
# img=cv2.resize(img, (750, 400), fx=1, fy=1)

# gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR2GRAY = BGR to GRAY從bgr轉換灰階圖片
# blur=cv2.GaussianBlur(img, (15, 15), 10) #gauss模糊(15, 15)中必為基數!
# canny=cv2.Canny(img, 100, 100) #抓圖中的邊緣輪廓

# cv2.imshow("img", img)
# cv2.imshow("gray", gray)
# cv2.imshow("canny", canny)
# cv2.waitKey(0)
#/////////////////////////////////////////////////////////////////////////

#圖片轉換HSV數值
# import numpy as np

# def empty(v): #創建函式
#     pass

# img=cv2.imread("pic.png") 
# img=cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# cap=cv2.VideoCapture(1) #開啟鏡頭偵測

# cv2.namedWindow("TrackBar") #建立動態控制條
# cv2.resizeWindow("TrackBar", 640, 320) #設定視窗的大小寬，高

# cv2.createTrackbar("Hue min", "TrackBar", 0, 179, empty) #Hue min為色調的最小值，trackbar圍在視窗的名稱，0控制條的初始值，197控制條的最大值
# cv2.createTrackbar("Hue MAX", "TrackBar", 179, 179, empty)
# cv2.createTrackbar("Sat min", "TrackBar", 0, 255, empty)
# cv2.createTrackbar("Sat MAX", "TrackBar", 255, 255, empty)
# cv2.createTrackbar("Val min", "TrackBar", 0, 255, empty)
# cv2.createTrackbar("Val MAX", "TrackBar", 255, 255, empty)
# hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #把每一偵的圖片都轉換成hsv

# while True: #written while迴圈
#     h_min=cv2.getTrackbarPos("Hue min", "TrackBar") #參數Hue min為控制條名稱，參數Trackbar為視窗的名稱
#     h_MAX=cv2.getTrackbarPos("Hue MAX", "TrackBar")
#     s_min=cv2.getTrackbarPos("Sat min", "TrackBar")
#     s_MAX=cv2.getTrackbarPos("Sat MAX", "TrackBar")
#     v_min=cv2.getTrackbarPos("Val min", "TrackBar")
#     v_MAX=cv2.getTrackbarPos("Val MAX", "TrackBar")
#     print(h_min, h_MAX, s_min, s_MAX, v_min, v_MAX)
#     # ret, img = cap.read() #先讀取每一偵的畫面，會回傳兩個值，一個是有沒有成功，另一個是每一偵的圖片
#     # hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #把每一偵的圖片都轉換成hsv
#     lower=np.array([h_min, s_min, v_min]) #創建一個最小值 
#     upper=np.array([h_MAX, h_MAX, h_MAX])#創建一個最大值
#     mask=cv2.inRange(hsv, lower, upper) #過濾顏色lower最小值, upper最大值
#     result=cv2.bitwise_and(img, img, mask=mask) # bitwise_and 來過濾想要顏色的函式

#     cv2.imshow("img", img)
#     cv2.imshow("hsv", hsv)
#     cv2.imshow("mask", mask)
#     cv2.imshow("result", result)
#     cv2.waitKey(1)
#/////////////////////////////////////////////////////////////////////////////////////////

#偵測圖形輪廓判斷式甚麼形狀
# img=cv2.imread("003.png")
# imgContours=img.copy() #複製一張圖，用來跑81行的for迴圈
# img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #偵測輪廓需先轉成灰階
# canny=cv2.Canny(img, 150, 200) #檢測邊緣，最低門檻值150, 最高門檻值200
# contours, hierarchy=cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #contours輪廓, hierarchy階層(用不到)， findContours用來偵測輪廓的函式，(canny要偵測的圖片, cv2.RETR_EXTERNAL使用的模式(此模式為偵測外廓), cv2.CHAIN_APPROX_NONE，為了保持輪廓點，所以不做壓縮動作)

# for cnt in contours:
#     cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 4) # -1是指抓每個輪廓，(255, 0, 0)用這個顏色去抓取出輪廓，4是指線的粗度
#     # print(cv2.contourArea(cnt)) #取得輪廓的面積
#     area=cv2.contourArea(cnt)#用面積來過濾噪點
#     if area>500:  #如果它的面積大於500
#         # print(cv2.arcLength(cnt, True)) #取得邊長，True是指圖形是有閉合的，不閉合為false
#         peri=cv2.arcLength(cnt, True) #輪廓的邊長命名為peri
#         vertices=cv2.approxPolyDP(cnt, peri*0.02, True) #用多邊形去近視輪廓，peri*0.02為近視值(近視值越大的話，這個多邊形的邊就會越多，則越小多邊形的邊就會越少)
#         corners=(len(vertices)) #取近視的多邊形頂點
#         x, y, w, h =cv2.boundingRect(vertices) #在判斷是哪種形狀之前，先把每個圖形都用方塊框起來
#         cv2.rectangle(imgContours, (x, y), (x+w,y+h), (0, 255, 0), 4) #(x+w,y+h)左上角座標加上這個的寬度,y座標加上這個的高度
#         if corners==3:
#             cv2.putText(imgContours, "triangle", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) #putText=寫上視窗，triangle三角形，(x,y-5)座標，cv2.FONT_HERSHEY_SIMPLEX字體，1=文字大小
#         elif corners==4:
#             cv2.putText(imgContours, "rectangle", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#         elif corners==5:
#             cv2.putText(imgContours, "pentagon", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#         elif corners>=6:
#             cv2.putText(imgContours, "circle", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# cv2.imshow("img", img)
# cv2.imshow("canny", canny)
# cv2.imshow("imgContours", imgContours)
# cv2.waitKey(0)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#偵測人臉
# img=cv2.imread("004.jpg")
# gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #載入辨識模型
# faceRect=faceCascade.detectMultiScale(gray, 1.1, 3) #detectMultiScale辨識人臉的函式，1.1為縮小的倍數，3相鄰的框最少要有幾個(越多偵測越嚴謹)
# print(len(faceRect))
# for(x, y, w, h)in faceRect:
#     cv2.rectangle(img, (x, y),(x+w,y+h), (0, 255, 0), 2)


# cv2.imshow("img", img)
# cv2.waitKey(0)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#這一段程式碼欠缺正常的HSV數值才能成功
import numpy as np
from pathlib import Path
cap=cv2.VideoCapture(0)

penColorHSV=[[86, 121, 205,111, 245, 255],
             [46, 78, 172,71, 255, 255],
             [22, 70, 214,31, 255, 255]] #這裡必須依照自己電腦當中用"HSV轉換數值程式"所跑出來的才準，同時也會依開啟螢幕的亮度有變化

penColorBGR=[[255,0,0],
             [0,255,0],
             [0,255,255] ] #這裡是讓畫面中判斷是甚麼顏色的筆就呈現甚麼顏色，然後寫penColorBGR[i]在cv2.circle當中

drawPoints=[]

def findPen(img):

    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #把每一偵的圖片都轉換成hsv

    for i in range(len(penColorHSV)):

        lower=np.array(penColorHSV[i][:3]) # 到123行的penColorHSV當中的0~3的值 
        upper=np.array(penColorHSV[i][3:6])#3~6的值
        mask=cv2.inRange(hsv, lower, upper) #過濾顏色lower最小值, upper最大值
        result=cv2.bitwise_and(img, img, mask=mask) # bitwise_and 來過濾想要顏色的函式
        penx, peny=findContours(mask)
        cv2.circle(imgContours, (penx, peny), 10, penColorBGR[i], cv2.FILLED )
        if peny!=-1:
            drawPoints.append([penx, peny, i])
        # cv2.imshow("result", result)
def findContours(img):
    contours, hierarchy=cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #contours輪廓, hierarchy階層(用不到)， findContours用來偵測輪廓的函式，(canny要偵測的圖片, cv2.RETR_EXTERNAL使用的模式(此模式為偵測外廓), cv2.CHAIN_APPROX_NONE，為了保持輪廓點，所以不做壓縮動作)
    x,y,w,h=-1,-1,-1,-1
    for cnt in contours:
        # cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 4) # -1是指抓每個輪廓，(255, 0, 0)用這個顏色去抓取出輪廓，4是指線的粗度
        area=cv2.contourArea(cnt)#用面積來過濾噪點
        if area>500:  #如果它的面積大於500
            peri=cv2.arcLength(cnt, True) #輪廓的邊長命名為peri
            vertices=cv2.approxPolyDP(cnt, peri*0.02, True) #用多邊形去近視輪廓，peri*0.02為近視值(近視值越大的話，這個多邊形的邊就會越多，則越小多邊形的邊就會越少)
            x, y, w, h =cv2.boundingRect(vertices) #在判斷是哪種形狀之前，先把每個圖形都用方塊框起來
    return x+h//2,y #顯示筆頭的頂點
def draw(drawPoints):
    for point in drawPoints:
        cv2.circle(imgContours, (point[0],point[1]), 10, penColorBGR[point[2]], cv2.FILLED)

while True:
    ret, frame=cap.read()
    if ret:
        imgContours=frame.copy()
        cv2.imshow("video", frame)
        findPen(frame)
        draw(drawPoints)
        cv2.imshow("contour", imgContours)
    else:
        break
    if cv2.waitKey(1)==ord("q"):
        break
