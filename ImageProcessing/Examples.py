import numpy as np
import cv2
import pandas as pd

#Example-h: This example captures an image while turning on the camera

import cv2

vid= cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

#Example-2: Generation an array using Numpy library
import numpy as np
import cv2
arr = np.array([1,2,3,4,5,6,8])
print(arr)
print(type(arr))
arr1=np.zeros((4,5))
print(arr1)
arr2=np.ones((4,1))
print(arr2)
arr3=np.ones((2,3)) *4
print(arr3)
arr4=np.arange(10,100,10)
print(arr4)
arr5=np.arange(10,100)
print(arr5)
arr6=np.arange(15).reshape(3,5)
print(arr6)

arr2d=np.arange(15).reshape(3,5)
arr3d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#ndim->It gives the number of size
#shape->It gives the size of array
#size->It gives the number of elements in the array
#dtype->It gives the type of elements in the array

print(arr2d.ndim)
print(arr3d.ndim)

print(arr2d.shape)
print(arr3d.shape)

print(arr2d.size)
print(arr3d.size)


print(arr2d.dtype)
print(arr3d.dtype)

#Type conversions
arr=np.array([1,2,3,4,5],np.uint8)
print(arr.dtype)
import pandas as pd

personal_list={'ad' : ['Eylül', 'Suna', 'Banu','Melih','Özan', 'Özgur'],
               'yas': [28,23,24,27,29,30],
               'maas':[6000,8000,4000,1500,5000,9000]}
print(type(personal_list))

















