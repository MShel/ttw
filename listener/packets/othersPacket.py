from listener.packets.abstractPacket import AbstractPacket

class OthersPacket(AbstractPacket):
   
    def __init__(self, binPacket: bytes, margin: int):
        self.binPacket = binPacket
        self.headerMargin = margin
        self.toPort = 'others'
        self.fromPort = 'others'
        self.data = ' '
        self.parse()
    
    def parse(self):
        pass
    
    def getName(self):
        return 'N/A protocol'