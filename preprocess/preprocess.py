## Using GLOB
#Now, let us load images and perform some action.
#import the opencv library so we can use it to read and process images
import cv2
import glob,os
#from skimage.filters import gaussian
#from skimage import img_as_ubyte

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

current_dir = 'data/obj'

# Percentage of images to be used for the test set
percentage_test = 10;

#select the path
path = "Dirt_dataset/obj/*.*"
#file_list = open('list.txt', 'w')
img_number = 1  #Start an iterator for image number.
#This number can be later added to output image file names.

for file in glob.glob(path):
    print(file)     #just stop here to see all file names printed
    img= cv2.imread(file, 0)  #now, we can read each file since we have the full path
    
    
    
    
#process each image - change color from BGR to RGB.
    #smoothed_image = img_as_ubyte(gaussian(img, sigma=5, mode='constant', cval=0.0))
    
    #cv2.imwrite("test_images/smoothed/smoothed_image"+str(img_number)+".jpg", smoothed_image)
    #img_number +=1 
    
    
    
    
    counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write("data/obj" + "/" + title + '.jpg' + "\n")
    #else:
        #file_train.write("data/obj" + "/" + title + '.jpg' + "\n")
     #   counter = counter + 1
