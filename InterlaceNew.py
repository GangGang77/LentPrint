import numpy as np
from PIL import Image

def interlace(intnum, lpi, OriginalDPI, OutputDPI, im1, im2, im3=None, im4=None):
    if (im3 is None and intnum > 2) or (im4 is None and intnum > 3):
        raise Exception('Not enough images')

    images = [im1, im2, im3, im4]
    image = im1
    pitch = 1/lpi * OriginalDPI

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

im1 = Image.open('CroppedOregon0.png')
im2 = Image.open('CroppedOregon41.png')
im3 = Image.open('CroppedOregon42.png')
im4 = Image.open('CroppedOregon-1.png')

OriginalDPI = 200
OutputDPI = 600
interlace(4, 50.17, dpi, im1, im2, im3=im3, im4=im4).save('Classic4Oregon.png', dpi=(OutputDPI, OutputDPI))
