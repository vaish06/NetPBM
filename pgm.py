# pgm.py 
# Your name here
# Your email here
# CSC 220, Fall 2016

from Netpbm import *

class PGM(Netpbm):
    '''Concrete Portable Gray Map file class.'''

    # MVM: API decision - the ctor either should take
    # no arguments OR have defaults for every parameter.
    # This is so the testing will work regardless of 
    # your design.
    def __init__(self):
       raise NotImplementedError

    # MVM: Override any methods you need to here.


if __name__=='__main__':
    # Assumes this is called from directory containing
    # sample_images sub-folder.
    try:
        print('-'*80)
        print('Calling constructor...')
        test = PGM()
        print('Reading sample_images/fungi.pgm...')
        test.read('sample_images/fungi.pgm')
        print('Writing a duplicate...')
        test.write('sample_images/copy-fungi.pgm')
        print('Inverting colors and writing copy...')
        inverted = test.invertColors()
        inverted.write('sample_images/inverted-fungi.pgm')
        print('Flipping left-right and writing copy...')
        leftRight = test.flipLR()
        leftRight.write('sample_images/left-right-fungi.pgm')
        print('Flipping top-bottom and writing copy...')
        topBottom = test.flipTB()
        topBottom.write('sample_images/top-bottom-fungi.pgm')
        print('Finished __main__, exiting.')
        print('-'*80)
    except Exception as e:
        print('Exception raised:')
        print(e)
