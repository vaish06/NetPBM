# Netpbm.py 
# Your name here
# Your email here
# CSC 220, Fall 2016

from Image import *

class Netpbm(Image):
    '''An "abstract" class for the Netbpm family of image files.
    Not intended to be instantiated.'''

    # MVM: Optional - you may change this to take parameters
    # depending upon your design. See the public interface
    # for hints about what
    def __init__(self):
        raise NotImplementedError

    # MVM: Optional - ~private interface/helper functions.
    # Depending upon your design, you might implement
    # helper methods. Indicate that by putting 1 underscore
    # in front of the name, e.g.:
    # def _helperMethod

    # MVM: Public interface
    def getMagicNumber(self):
        raise NotImplementedError    

    def getMaxVal(self):
        raise NotImplementedError

    def setMaxVal(self, maxval):
        raise NotImplementedError

    def setMagicNumber(self):
        raise NotImplementedError

    # MVM: This can probably be implemented here and work for
    # all three of PBM, PGM, and PPM
    def __repr__(self):
        raise NotImplementedError

    # MVM: depending upon your design, you may need to implement
    # some of the methods inherited from Image in this class.

if __name__=='__main__':
    print('Netpbm is an abstract class.')
