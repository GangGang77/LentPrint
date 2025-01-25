from PIL import Image
import numpy as np
from PIL import ImageDraw


def pitch_test(lpi, w, h, dpi):
    wip = int(w * dpi)
    hip = int(h * dpi)
    pixels = np.zeros((wip, hip))
    pitch = 1/lpi * dpi
    for x in range(wip):
        if x % (pitch) < pitch / 2:
            pixels[x, :] = 255
    return pixels

def pitch_selection(lpi, inc, samples, w, h, dpi):
    min = lpi - (inc * samples / 2)
    max = lpi + (inc * samples / 2)
    pixels = np.full((w * dpi, int(h * dpi / 4 / samples)), 255)
    testh = h / samples
    pitchRange = np.arange(min, max, inc)
    for i in pitchRange:
        pixels = np.concatenate((pixels,
                                 pitch_test(i, w, testh, dpi),
                                 np.full((w * dpi, int(h * dpi / 4 / samples)), 255)), axis=1)
    pixels = np.concat((pixels,
                        np.full((int(h * dpi / samples / 4),pixels.shape[1]), 255),
                        np.zeros((int(1/lpi * dpi), pixels.shape[1])),
                        np.full((int(h * dpi / samples), pixels.shape[1]), 255)), axis=0)
    image = Image.fromarray(pixels)
    labels = ImageDraw.Draw(image)
    for i in range(samples):
        labels.text((int(pixels.shape[1] * (i + .25) / (samples + .125)),
                     pixels.shape[0] - int(h * dpi / samples / 1.5)), str(round(pitchRange[i], 2)), font_size=(h * dpi / samples / 3))
    return image



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lpi = 50
    inc = .05
    samples = 100
    w = 4
    h = 35
    dpi = 600
    image = pitch_selection(lpi, inc, samples, w, h, dpi)
    image.show()


