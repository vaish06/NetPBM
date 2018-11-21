# project1.py
# Your name here
# Your email here
# CSC 220, Fall 2016

# Call this on the command line like:
# python3 projec1.py image.pnm


from Image import *
from Netpbm import *
from pbm import *
from pgm import *
from ppm import *

import sys
import os.path

if __name__=='__main__':
    try:
        imgfilepath = sys.argv[1]
        imgbasename = os.path.basename(imgfilepath)
        imgtype = imgbasename[-3:]
        
        if (imgtype == 'pbm'):
            img = PBM()
        elif (imgtype == 'pgm'):
            img = PGM()
        elif (imgtype == 'ppm'):
            img = PPM()
        else:
            raise ValueError('Unknown file extension.')
    
        img.read(imgfilepath)
        print(img)
        inv = img.invertColors()
        flip = inv.flipLR()
        flip.write('inv-flip-'+imgbasename)
    except Exception as e:
        print('Exception raised:')
        print(e)
