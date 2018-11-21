# Image.py 
# Your name here
# Your email here 
# CSC 220, Fall 2016

class Image:
    '''An "abstract" base class for generic image data.
    Not intended to be instantiated.'''

    # MVM: Supply a constructor. See the Public API for
    # hints about what private data members Image should have.
    # Optional: You may change this to take parameters if your design
    # needs it.
    def __init__(self):
        # MVM: See the recommendations in the spec for different
        # approaches on how to store the pixel data.
        pass

    # MVM: Public interface - some of these may be implemented
    # here, some might be implemented in derived classes.
    def getWidth(self):
        raise NotImplementedError

    def getHeight(self):
        raise NotImplementedError 

    def getPixels(self):
        raise NotImplementedError 

    def getChannels(self):
        raise NotImplementedError

    def setWidth(self, width):
        raise NotImplementedError

    def setHeight(self, height):
        raise NotImplementedError

    def setPixels(self, pixels):
        raise NotImplementedError

    def setChannels(self, channels):
        raise NotImplementedError
   
    def write(self):
        '''Public API for writing an image file.'''
        raise NotImplementedError

    def read(self):
        '''Public API for reading an image file.'''
        raise NotImplementedError

    # MVM: When implementing, have these return copies of
    # the Image objects - helps avoid having a user
    # write over the original image file.
    # Hint: see the last part of the OOP II webnotes.
    def flipLR(self):
        '''Flips image left-right.'''
        raise NotImplementedError

    def flipTB(self):
        '''Flips image top-bottom.'''
        raise NotImplementedError 

    def invertColors(self):
        '''Inverts image colors.'''
        raise NotImplementedError

    def LumaCode(self):
        '''Luma codes color image for video.'''
        raise NotImplementedError

    def extractChannel(self, channel):
        '''Extracts a given channel from a color image.'''
        raise NotImplementedError

if __name__=='__main__':
    print('Image is an abstract base class.')
