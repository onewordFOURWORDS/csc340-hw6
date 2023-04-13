import math

import cv2 as cv
import numpy as np


def create_filter(size, sigma):
    filter = np.zeros((size,size), np.float32)
    for x in range((-size//2),size//2+1):
        for y in range(-size//2,size//2+1):
            # gaussian calculation 
            filter[x+size//2][y+size//2] = (1/(2*math.pi*sigma**2))*math.exp(-(x**2+y**2)/(2*sigma**2))

    # The corner of the filter should equal 1
    magnitude = 1 / filter[0][0] 
    filter = filter * magnitude
    filter = filter.round(2)

    return filter

def get_image(image_name):
    image = cv.imread(image_name)
    return image

def guassian_blur(image, filter):
    filter_size = filter.shape[0] 
    filter_sum = np.sum(filter)

    image_height = image.shape[0]
    image_width = image.shape[1]

    new_image = np.zeros((image_height, image_width, 3), np.float32)

    border = filter_size//2 
    for x in range(border, image_width - border):
        for y in range(border, image_height - border):
            # get submatrix of the image
            subimage = image[y-border:y+border+1, x-border:x+border+1]

            # multiply the subimage with the filter
            subimage = subimage * filter/filter_sum

            # sum the values of the subimage
            # subimage = np.sum(subimage)

            # set the pixel to the new value
            for color in range(3):
                new_image[y][x][color] = np.sum(subimage[color])
            cv.waitKey(0)

    return new_image


def main():
    filter = create_filter(3, 1.5)
    image = get_image("tripod.jpg")

    # blur the image with the filter
    blurred_image = guassian_blur(image, filter)

    # show the blurred image
    cv.imshow("blurred image", blurred_image)
    cv.waitKey(0)



if __name__ == "__main__":
    main()


