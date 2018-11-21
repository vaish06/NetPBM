# pbm.py 
# Your name here
# Your email here
# CSC 220, Fall 2016

from Netpbm import *

class PBM(Netpbm):
    '''Concrete Portable Bit Map file class.'''

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
        test = PBM()
        print('Reading sample_images/G.pbm...')
        test.read('sample_images/G.pbm')
        print('Writing a duplicate...')
        test.write('sample_images/copy-G.pbm')
        print('Inverting colors and writing copy...')
        inverted = test.invertColors()
        inverted.write('sample_images/inverted-G.pbm')
        print('Flipping left-right and writing copy...')
        leftRight = test.flipLR()
        leftRight.write('sample_images/left-right-G.pbm')
        print('Flipping top-bottom and writing copy...')
        topBottom = test.flipTB()
        topBottom.write('sample_images/top-bottom-G.pbm')
        print('Finished __main__, exiting.')
        print('-'*80)
    except Exception as e:
        print('Exception raised:')
        print(e)
