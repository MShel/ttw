from abc import ABCMeta, abstractmethod

class AbstractProtocol:
    __metaclass__ = ABCMeta

    @abstractmethod
    def parsePacket(self):
        pass
        
    @abstractmethod
    def writePacket(self):
        pass

    @abstractmethod
    def decryptData(self):
        pass
    
    @abstractmethod
    def writeToLog(self,logFormat='%%PROTOCOL%%,%%ADDRESS%%,%%PORT%%'):
        pass
