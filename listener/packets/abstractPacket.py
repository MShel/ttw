from abc import ABCMeta, abstractmethod

class AbstractPacket:
    
    __metaclass__ = ABCMeta
    
    STATUS_INITIATED = 'INITIATED'
    
    STATUS_PARSED = 'PARSED'
    
    def __init__(self):
        self.verbose = False
        self.status = None
        
    @abstractmethod
    def parse(self):
        pass
        
    @abstractmethod
    def writePacket(self):
        pass

    @abstractmethod
    def decryptData(self):
        pass
    
    def writeToLog(self, logger, logFormat='%%PROTOCOL%%,%%ADDRESS%%,%%PORT%%'):
        logger.log(self.parsedPacket, logFormat)
        pass
    
    def setVerbose(self, verbose: bool):
        self.verbose = verbose
        
    def getVerbose(self):
        return self.verbose
    