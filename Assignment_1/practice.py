import keras 
from mp1 import *
import matplotlib.pyplot as plt
from PIL import Image
import sys

IMAGE_SIZE = 100
X_train, Y_train = generate_dataset_classification(300, 20)

print X_train.shape
print Y_train.shape

Train_directory = './Train_Images/'

# Save the Images
count = 0
for im in X_train:
	count = count + 1
	im = im.reshape(IMAGE_SIZE,IMAGE_SIZE)
	#plt.imshow(im.reshape(IMAGE_SIZE,IMAGE_SIZE), cmap='gray')
	plt.imsave(Train_directory + 'train_image_'+str(count)+'.jpg',im,cmap='gray')