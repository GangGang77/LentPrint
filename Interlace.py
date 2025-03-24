import numpy as np
from PIL import Image

def interlace(intnum, lpi, dpi, im1, im2, im3=None, im4=None):
    if (im3 is None and intnum > 2) or (im4 is None and intnum > 3):
        raise Exception('Not enough images')

    images = [im1, im2, im3, im4]
    image = im1
    pitch = 1/lpi * dpi

    for i in range (1, intnum):
        mask_array = np.full((im1.size), 255, dtype='uint8').transpose()

        for j in range (im1.size[0]):
            print(str(j) + ', ' + str(pitch) + ', ' + str(j % pitch) + ', ' + str((pitch / intnum)*i))
            if j % pitch > (pitch / intnum) * i:
                mask_array[:, j] = 0
        mask = Image.fromarray(mask_array, mode='L')
        image = Image.composite(image, images[i], mask)
        #mask.show()

    return image

im1 = Image.open('red.png')
im2 = Image.open('green.png')
im3 = Image.open('blue.png')
im4 = Image.open('white.png')

dpi = 200
interlace(4, 50.17, dpi, im1, im2, im3=im3, im4=im4).save('solidTest4.png', dpi=(dpi, dpi))
