from PIL import Image
import os
img_size = (125, 125)

for fil in os.listdir('.'):
    if fil.endswith('.jpg'):
        img = Image.open(fil)
        img.thumbnail(img_size)
        img.save('profile.jpg')
