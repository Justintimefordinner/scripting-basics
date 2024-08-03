import os
import eyed3
import string
import random

#WIP attempt at randomizing file names
path = None

for filename in os.listdir(path):
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=10))
    my_dest = str(res)+".mp3"
    my_source = path + filename
    my_dest = path + my_dest
    os.rename(my_source, my_dest)
