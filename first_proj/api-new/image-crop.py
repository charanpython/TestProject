'''
Created on May 28, 2018

@author: Charan
'''
from PIL import Image
try:
    img = Image.open("E:\\FAMILY TOUR PHOTOS\\DSC01803.JPG")
#     img2 = Image.open("E:\\FAMILY TOUR PHOTOS\\DSC01833.JPG")
  
except IOError:
    pass
else:
#     img = img.rotate(160)
#     img.paste(img2,(0,0))
#     img = img.transpose(Image.FLIP_TOP_BOTTOM)
#     img.save("E:\\charan\\edit.png")
    img = img.crop((0,0,600,600))
    img.show()
    