import image
import matplotlib.pyplot as plt
import pandas as pd
import image
#scatter() is used for point graphics
#hist() is used for histogram graphicst it is the name that correspond to data)
import cv2
import matplotlib.pyplot as plt

image= cv2.imread('1.jpg')  #capturing the img
image= cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE) #It is return the image in grey.
image= cv2.imread('1.jpg',0) #Same
cv2.imshow('Profile',image)
cv2.waitKey(0)  #It is wait for the input(data) from keyboard
kInp=cv2.waitKey(0)  #It is usually used for videos
if kInp == 65:
    print('Klavyeden büyük A harfine basıldı.')
else:
    print('Klavyeden başka bir harfe basıldı. ')
kInp=cv2.waitKey(0)    #Returns ASCI corresponding
print(kInp)
if kInp == ord('a'):
    print('Klavyeden a harfine basıldı.')
else:
    print('Klavyeden başka bir harfe basıldı. ')
cv2.destroyAllWindows()
image= cv2.imread('1.jpg')
cv2.imwrite('5.png',image)  #This process works to saving or writing the images
#Turn on the camera
video=cv2.VideoCapture(0)  #This object is belongs to computer.We will take frames and than show this frames in the screen using loops
while True:
    ret,frame=video.read()
    cv2.imshow('videom',frame)
    kInp= cv2.waitKey(20)
    if kInp==ord('q'):
        break
video.release()  #It means disconnection the computer with main camera
cv2.destroyAllWindows()  #Close all screens about opencv

#Capturing video
video=cv2.VideoCapture(0)  #We can see the properties of our image(video object) that we catched
w=int(video.get(3))
h=int(video.get(4))
size=(w,h)
result=cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'XVID'),24,size) #It is consists of 4 parameter. They are file name.extension, piksel format,24 fps and size

while True:
    ret, frame=video.read()
    if ret==True:
        result.write(frame)
        cv2.imshow('Videom',frame)
        kInp = cv2.waitKey(1)
        if kInp == ord('s'):
            break
    else:
        break
video.release()
result.release()
cv2.destroyAllWindows()
#Picture Features

image =cv2.imread('1.jpg')
#Using item we can capture the color value of any pixel in the image at any point.
#Using imread() when we read the image, we will read the image in BGR format
print('Blue:', image.item(10,10,0))
print(image[300,200])
#itemset is using for changing the image's value in any point.
image.itemset(10,10,2,0)
cv2.imshow('resim',image)
for x in range(50):
        for y in range(50):
            image.itemset(x, y, 0, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()
#shape is help us to see the sizes of our image
print(image.shape)
#size shows the number of piksels (or the minus value of y , x and c)
print(image.size)
#datatype
print(image.dtype) #-> uint8
#ROI taking a piece from image
#roi=[y1:y2,x1:x2]
roi=image[154 : 190 , 126 : 180]
cv2.imshow('idk',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Color filter can destroy any color that you want or we can make it dominant
#When we determine a piksel the meaning of ':' is all
#image[:,:,2] =0 #BGR  cyan
image[:,:,0] =255 #We will expect to see the image in white with this three row
image[:,:,1] =255
image[:,:,2] =255
cv2.imshow('pic',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Methods for image framing
#BORDER_REPLİCATE expanded the last parts of the original pixel
#BORDER_REFLECT_101
#BORDER_REFLECT can create a mirror image
#BORDER_WRAP can multiply the same image
#BORDER_CONSTANT can create frame with 20px size and green
image =cv2.imread('1.jpg')
replicate=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_REPLICATE)
reflect= cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_REFLECT)
reflect_101=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_REFLECT_101)
wrap=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_WRAP)
greenColor=[0,255,0]
constant=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=greenColor) #In addition it wants a color parameter

cv2.imshow('main',image)
cv2.imshow('replicate',replicate)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.subplot(2,3,1) , plt.imshow(image) , plt.title('Original')
#subplots(how many row,how many column, index) we have 6 image so 2x3
plt.subplot(2,3,2) , plt.imshow(replicate) , plt.title('REPLİCATE')
plt.subplot(2,3,3) , plt.imshow(reflect) , plt.title('REFLECT')
plt.subplot(234) , plt.imshow(reflect_101) , plt.title('REPLİCATE_101')
plt.subplot(235) , plt.imshow(wrap) , plt.title('WRAP')
plt.subplot(2,3,6) , plt.imshow(constant) , plt.title('CONSTANT')
plt.show()
#Sizing and Cropping
import cv2
image =cv2.imread('1.jpg')
#print('orijinal',image.shape)
imageResized=cv2.resize(image,(250,150)) #This method is used for resizing the image
cv2.imshow('sized',imageResized)
cv2.waitKey(0)
cv2.destroyAllWindows()
#To increase the official 1.1/2 times
y,x,c=image.shape
imageResized=cv2.resize(image,(x+x//2,y+y//2))
cv2.imshow('sized',imageResized)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Cropping(ROI)
cropped=image[0:200,0:150]
cv2.imshow('cropped',cropped)
#Dividing the picture into parts and combining them (for instance into 4 parts)
y,x,c=image.shape
cropped=image[0:y//2,0:x//2]
cv2.imshow('cropped',cropped)
cropped1=image[0:y//2,x//2:x]
cv2.imshow('cropped1',cropped1)
cropped2=image[y//2:y,0:x//2]
cv2.imshow('cropped2',cropped2)
cropped3=image[y//2:y,x//2:x]
cv2.imshow('cropped3',cropped3)
#cropped=image[0:y//2,0:x//2]
#cropped=image[0:y//2,0:x//2]

cv2.waitKey(0)
cv2.destroyAllWindows()
#Mixing the pictures :Normal adding vs arithmetic addition
import cv2

image3=cv2.imread('3.jpg')
#totalImage=cv2.add(image,image3) #This value is holding the combining status, with add method.Error occures
#Reason is, They have to have the same pixsel size when we want to combine them
print('img:',image.shape)
print('img3:',image3.shape)






