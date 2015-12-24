from listener.packets.abstractPacket import AbstractPacket
import socket
from struct import unpack

class IpPacket(AbstractPacket):
    
    UNPACK_FORMAT = '!BBHHHBBH4s4s'
    IP_HEADER_LENGTH = 20
    
    def __init__(self, binPacket, ehl):
        self.ethernetHeaderLength = ehl
        self.binPacket = binPacket
        self.parse()
    
    def parse(self):
        
        AbstractPacket.addMsg(AbstractPacket, 'Started Parsing IP packet')
        binIpHeader = self.binPacket[self.ethernetHeaderLength:self.ethernetHeaderLength + 20]
        
        ipHeader = unpack(self.UNPACK_FORMAT , binIpHeader)
       
        binVersion = ipHeader[0]
        self.version = binVersion >> 4
        headerLengthBin = binVersion & 0xF
        self.iphLength = headerLengthBin * 4
        
        self.ttl = ipHeader[5]
        self.protocol = ipHeader[6]
        self.fromAddress = str(socket.inet_ntoa(ipHeader[8]));
        self.toAddress = str(socket.inet_ntoa(ipHeader[9]));
        
        AbstractPacket.addMsg(AbstractPacket, 'Parsed IP packet from: ' + self.fromAddress + ' to: ' + self.toAddress)
