from listener.packets.abstractPacket import AbstractPacket

class AbstractAdapter:
    
    def __init__(self, credentials: dict):
        pass
    
    def recordPacket(self,packet:AbstractPacket):
        pass
    
    def executeSchema(self):
        pass