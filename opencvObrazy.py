import cv2

img1 = cv2.imread("C:\\obrazy\\julia.jpg",1)
img1 = cv2.resize(img1,(800,800))#width, height
print(img1)
cv2.imshow("original",img1)

#cv2, grayscale
img2 = cv2.imread("C:\\obrazy\\julia.jpg",0)
img2 = cv2.resize(img2,(800,800))#width, height
cv2.imshow("Gray Scale Image",img2)
print("Image in gray scale==\n", img2)

#cv2, grayscale
img3 = cv2.imread("C:\\obrazy\\julia.jpg",-1)
img3 = cv2.resize(img3,(800,800))#width, height
cv2.imshow("Oryginal-unchange Image",img3)
print("Image in gray scale==\n", img3)


cv2.waitKey()
cv2.destroyAllWindows()
