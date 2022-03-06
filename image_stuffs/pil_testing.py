from PIL import Image
import numpy as np
from PyImage import PyImage as pImg

def random_img(output, width, height):

  array = np.random.randint(0, 255, (height,width,3))  

  array = np.array(array, dtype=np.uint8)
  img = Image.fromarray(array)
  img.save(output)

def pyImgTesting():
  img = pImg(16, 32)
  img.randomize()

  print(img[0][0])
  img[1][1] = np.array([0., 1., 0.])

  img.save('out/pyImg_test.png')
  img.stretch(8)
  img.save('out/pyImg_test2.png')

def main():
  pyImgTesting()
  # random_img('out/random.png', 100, 50)

  # image = Image.open('in/test_in.png')
  # img = np.asarray(image)
  # print(img.shape)

  # npOut = np.empty([32, 32, 3], dtype=np.uint8)

  # for row in range(32):
  #   for col in range(32):
  #     npOut[row][col] = img[row * 8][col * 8]
  
  # imOut = Image.fromarray(npOut)
  # imOut.save('out/test.png')

  # pxMap = image.load()
  # print(pxMap)
  # print(pxMap[0,0])
  # pxMap[0,0] = (255, 0, 0)
  # image.save('in/test_out.png')

main()