class AbstractFactory:
    
    #schema - sql database structure, json - mongoDb, etc
    schema = ''
     
    @staticmethod
    def factory(packetType: int, binPacket: bytes, margin):
        pass
    
    @staticmethod
    def buildSchema(self, adapter):
        pass 