from listener.packets.abstractPacket import AbstractPacket
from stats.adapters.abstractAdapter import AbstractAdapter

class MysqlAdapter(AbstractAdapter):
    
    def recordPacket(self,packet:AbstractPacket):
        pass
    
    def executeSchema(self):
        pass