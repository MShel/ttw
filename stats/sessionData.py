from listener.packets.abstractPacket import AbstractPacket
import json

class SessionData:
    
    def __init__(self):
        self.totalCounter = 0
        self.fromCounter = {}
        self.toCounter = {}
        self.portOutCounter = {}
        self.portInCounter = {}
        self.protocolStat = {}
        self.counterFrom = 0
        self.toAddress = 0
        self.toPort = 0
        self.fromPort = 0
        self.prName = 0 
        
    '''
    parentPacket - internet layer (IP)
    childPacket - the transport layer packet(TCP/IP)
    '''
    def addPacket(self, parentPacket:AbstractPacket, childPacket:AbstractPacket):
        self.totalCounter += 1 

        
        if(self.fromCounter.get(parentPacket.fromAddress) == None): self.counterFrom += 1
        self.fromCounter.update({parentPacket.fromAddress:self.counterFrom})
        
        if(self.fromCounter.get(parentPacket.toAddress) == None): self.toAddress += 1
        self.toCounter.update({parentPacket.toAddress:self.toAddress})
       
        if(self.fromCounter.get(childPacket.toPort) == None): self.toPort += 1
        self.portOutCounter.update({childPacket.toPort:self.toPort})
        
        if(self.fromCounter.get(childPacket.fromPort) == None): self.fromPort += 1
        self.portInCounter.update({childPacket.fromPort:self.fromPort})

        if(self.fromCounter.get(childPacket.getName()) == None): self.prName += 1
        self.protocolStat.update({childPacket.getName():self.prName})
     
    def jsonify(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)    
