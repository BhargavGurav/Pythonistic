import cv2

# getting size of image
image = cv2.imread('mypic.JPG')  # path to image
dimensions = image.shape
print(f"width x height :  {dimensions[1]} x {dimensions[0]}")


# resizing image
image = cv2.imread('mypic.JPG', 1)
new = cv2.resize(image, (300, 400))  # resize to the given parameters
cv2.imshow('resized image', new)
cv2.waitKey(0)                       # to stop display window 
cv2.destroyAllWindows()


