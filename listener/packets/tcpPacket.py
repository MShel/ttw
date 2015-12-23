from listener.packets.abstractPacket import AbstractPacket
from listener.packets.ipPacket import IpPacket

class TcpPacket(IpPacket):
    
    
    def __init__(self,binPacket):
        self.parsedPacket = []
        self.binPacket = binPacket
        self.status = self.STATUS_INITIATED
        self.parse()
    
    def parse(self):
        self.addMsg('Started Parsing TCP packet')
            
       
    def getMsg(self):
        return self.msg
    
    def addMsg(self, msg:str):
        self.msg = self.getMsg()+'\n'+msg
        return self.msg
    
    def __del__(self):
        pass
    
