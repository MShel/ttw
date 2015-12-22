from listener.packets.abstractPacket import AbstractPacket

class TcpPacket(AbstractPacket):
    def __init__(self):
        self.msg = ''
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
    
