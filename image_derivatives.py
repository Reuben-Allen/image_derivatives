"""
Reuben Allen
8/18/2021

This program finds image derivatives using 2D convolution with filters.
"""

# import python libraries
import numpy as np
import math
import cv2
import argparse
from tqdm import tqdm
from PIL import Image

# define 2D convolution function (edge padding)
def discrete_2D_convolution(kernel, image):
    # find kernel size and pad the image using edge values
    kernel_width = [math.floor(x/2) for x in kernel.shape]
    pad_image = np.pad(image, ((kernel_width[0],kernel_width[0]),(kernel_width[1],kernel_width[1])), 'edge')
    result = np.zeros(pad_image.shape)

    # perform image convolution
    kernel_transform = np.fliplr(np.flipud(kernel))
    for i in tqdm(range(kernel_width[0],pad_image.shape[0]-kernel_width[0]), desc="Loading..."):
        for j in range(kernel_width[1],pad_image.shape[1]-kernel_width[1]):
            partition = pad_image[i-kernel_width[0]:1+i+kernel_width[0],j-kernel_width[1]:1+j+kernel_width[1]]
            result[i,j] = np.sum(np.multiply(partition,kernel_transform))
    return result

# define image gradient function
def gradient(dx,dy):
    return np.sqrt(np.add(np.power(dx,2),np.power(dy,2)))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Find image derivatives.')
    parser.add_argument('--image', type=str, required=True, help='Full path to image file')
    args = parser.parse_args()

    # define convolution kernel
    fx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    fy = np.transpose(fx)

    # load image and transform to grayscale
    image = cv2.imread(args.image,0)
    image = cv2.bilateralFilter(image,9,75,75)

    # utilize gradient and convolution functions
    dx = discrete_2D_convolution(fx, image)
    dy = discrete_2D_convolution(fy, image)
    gradient_im = gradient(dx,dy)

    pil_image = Image.fromarray(gradient_im)
    pil_image.show()