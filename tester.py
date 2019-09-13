from sum import *
import random
from random import *
def test_sum():

    for i in  range(0, 100):
      x = uniform(-100, 100)
      y = uniform(-100, 100)
      assert(get_sum(x, y) == x + y)
      print(get_sum(x,y))