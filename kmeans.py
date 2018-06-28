#Author:xiao luo
from sklearn.cluster import KMeans
import cv2
import numpy as np

num_class = 4
image = cv2.imread("D:\\123.jpg",1)
image=cv2.resize(image,(1000,1000))
cv2.imshow("src",image)
data = image.reshape(image.shape[0]*image.shape[1],3)#将图像每个像素作为一个样本，作为kmeas的输入
kmeans = KMeans(num_class)
kmeans.fit(data)
labels = kmeans.labels_#获取label
for j in range(image.shape[0]):
    for i in range(image.shape[1]):
        index = i+j*image.shape[1]#计算对应的label索引
        if labels[index] == 0:
            image[j][i][0]=0
            image[j][i][1] = 255
            image[j][i][2] = 0
        elif labels[index] == 1:
            image[j][i][0]= 255
            image[j][i][1] = 0
            image[j][i][2] = 0
        elif labels[index] ==2:
            image[j][i][0] = 0
            image[j][i][1] = 0
            image[j][i][2] = 255
        elif labels[index] == 3:
            image[j][i][0] = 0
            image[j][i][1] = 0
            image[j][i][2] = 0
cv2.imshow("result",image)
cv2.imwrite("result.bmp",image)
cv2.waitKey(0)