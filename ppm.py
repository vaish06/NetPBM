# ppm.py 
# Your name here
# Your email here
# CSC 220, Fall 2016

from Netpbm import *

class PPM(Netpbm):
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
        test = PPM()
        print('Reading sample_images/cropped-purple_coneflowers.ppm...')
        test.read('sample_images/cropped-purple_coneflowers.ppm')
        print('Writing a duplicate...')
        test.write('sample_images/copy-cropped-purple_coneflowers.ppm')
        print('Inverting colors and writing copy...')
        inverted = test.invertColors()
        inverted.write('sample_images/inverted-cropped-purple_coneflowers.pbm')
        print('Flipping left-right and writing copy...')
        leftRight = test.flipLR()
        leftRight.write('sample_images/' \
                'left-right-cropped_purple_coneflowers.ppm')
        print('Flipping top-bottom and writing copy...')
        topBottom = test.flipTB()
        topBottom.write('sample_images/' \
                'top-bottom-cropped-purple_coneflowers.ppm')
        print('Luma coding image...')
        luma = test.LumaCode()
        luma.write('sample_images/' \
                'luma-cropped-purple_coneflowers.ppm')
        print('Extracting red channel...')
        red = test.extractChannel('red')
        red.write('sample_images/' \
                'red-cropped-purple_coneflowers.pgm')
        print('Extracting green channel...')
        green = test.extractChannel('green')
        green.write('sample_images/' \
                'green-cropped-purple_coneflowers.pgm')
        print('Extracting red channel...')
        blue = test.extractChannel('blue')
        blue.write('sample_images/' \
                'red-cropped-purple_coneflowers.pgm')
        print('Finished __main__, exiting.')
        print('-'*80)
    except Exception as e:
        print('Exception raised:')
        print(e)
