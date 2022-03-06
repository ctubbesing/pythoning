from PIL import Image
import numpy as np

class PyImage:
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.pxMat = np.zeros((rows, cols))
  
  def __getitem__(self, idx):
    return self.pxMat[idx]
  
  def stretch(self, stretchAmt):
    self.rows *= stretchAmt
    self.cols *= stretchAmt
    self.pxMat = np.repeat(np.repeat(self.pxMat, stretchAmt, axis=0), stretchAmt, axis=1)
  
  def randomize(self):
    self.pxMat = np.random.random_sample((self.rows, self.cols, 3))
  
  def save(self, filename):
    array = np.array(self.pxMat * 255, dtype=np.uint8)
    img = Image.fromarray(array)
    img.save(filename)