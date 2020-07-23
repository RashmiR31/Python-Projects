import cv2
import numpy as np
import sys
import os
import fnmatch

def sharpen(image):
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    sharp_image=cv2.filter2D(image,-1,kernel)
    cv2.imshow('Sharpened image',sharp_image)
    cv2.waitKey(0)
    return sharp_image

def blur(image):
    kernels=[3,5,9,13]
    for idx,k in enumerate(kernels):
        image_blur=cv2.blur(image,ksize=(k,k))
        cv2.imshow(str(k),image_blur)
        cv2.waitKey(0)

def resize(fname,width,height):
    image = cv2.imread(fname)
    cv2.imshow('Original Image',image)
    cv2.waitKey(0)
    org_height,org_width=image.shape[0:2]
    print('width:',org_width)
    print('height:',org_height)
    
    if org_width >= org_height:
        new_image=cv2.resize(image,(width,height))
    else:
        new_image=cv2.resize(image,(height,width))
    
    return fname, new_image

'''Now this is for batch processing of images where 
each image in a directory is processed, resized and added to a new folder'''
listoffiles=os.listdir('.')
pattern='*.jpg'
n=len(sys.argv)
if n==3:
    width=int(sys.argv[1])
    height=int(sys.argv[2])
else:
    width=1280
    height=960

if not os.path.exists('new_folder'):
    os.makedirs('new_folder')
for filename in listoffiles:
    if fnmatch.fnmatch(filename,pattern):
        filename,new_image=resize(filename,width,height)
        cv2.imwrite('New_folder\\'+filename,new_image)
''' This is the end of batch processing code'''        
    
#filename,new_image=resize('Capture.jpg',1280,960)'''This is a function call to the resize function'''
#cv2.imshow('Resized image',new_image)'''To show the resized image'''
#cv2.waitKey(0)'''to display the resized imaage'''
#blur(new_image)'''Function call to blur the image'''
#image=sharpen(new_image)'''function call to sharpen the image'''