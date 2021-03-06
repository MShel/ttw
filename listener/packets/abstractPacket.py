from abc import ABCMeta, abstractmethod
import string

class AbstractPacket:
    
    __metaclass__ = ABCMeta
    
    msg = ''
    
    STATUS_INITIATED = 'INITIATED'
    
    STATUS_PARSED = 'PARSED'
    
    toAddress = ''
    
    fromAddress = ''
    
    def __init__(self):
        self.verbose = False
        self.status = None
        self.msg=''
        
    @abstractmethod
    def parse(self):
        pass
    
    @abstractmethod
    def getName(self):
        pass
           
    def decryptData(self):
        pass
    
    def writeToLog(self, logger, logFormat='%%PROTOCOL%%,%%ADDRESS%%,%%PORT%%'):
        logger.log(self.parsedPacket, logFormat)
        pass
    
    def setVerbose(self, verbose: bool):
        self.verbose = verbose
        
    def getVerbose(self):
        return self.verbose
    
    def getMsg(self):
        return self.msg
    
    def addMsg(self, msg:str):
        AbstractPacket.msg = AbstractPacket.getMsg(AbstractPacket)+'\n'+msg
        return AbstractPacket.msg   
    
    @staticmethod
    def getPrintable(data):
        result = ''.join(filter(lambda x: x in string.printable, data))
        return result