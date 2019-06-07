from PIL import Image
from PIL import ImageFilter
import numpy as np
im0=np.array(Image.open('9.jpg').convert('L'))
im1=255-im0
im2=(100/255)*im0+150#灰白滤镜
im3=255*(im1/255)**2
pil_im=Image.fromarray(np.uint(im2))
pil_im.show()
pil_im.save('99.gif')