from listener.packets.abstractPacket import AbstractPacket
import socket
from struct import *

class IpPacket(AbstractPacket):
    
    UNPACK_FORMAT = '!BBHHHBBH4s4s'
    
    def __init__(self, binPacket, ehl):
        self.ethernetHeaderLength = ehl
        self.parsedPacket = []
        self.binPacket = binPacket
        self.status = self.STATUS_INITIATED
        self.parse()
    
    def parse(self):
        AbstractPacket.addMsg(AbstractPacket, 'Started Parsing IP packet')
        ip_header = self.binPacket[self.ethernetHeaderLength:20 + self.ethernetHeaderLength]
        # now unpack them :)
        iph = unpack(self.UNPACK_FORMAT , ip_header)
        version_ihl = iph[0]
        self.version = version_ihl >> 4
        ihl = version_ihl & 0xF
        self.iph_length = ihl * 4
        self.ttl = iph[5]
        self.protocol = iph[6]
        self.s_addr = socket.inet_ntoa(iph[8]);
        self.d_addr = socket.inet_ntoa(iph[9]);