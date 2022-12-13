from functions import *

print(reduce(lambda x, y: x + "\n" + y, readlines("self.py")))