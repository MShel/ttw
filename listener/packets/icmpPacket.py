from listener.packets.abstractPacket import AbstractPacket
from struct import unpack

class IcmpPacket(AbstractPacket):
    
    UNPACK_FORMAT = '!BBH'
    ICMP_HEADER_LENGTH = 4
    PROTOCOL_NAME = 'ICMP'
    
    def __init__(self, binPacket: bytes, margin: int):
        self.binPacket = binPacket
        self.headerMargin = margin
        self.toPort = 'ICMP'
        self.fromPort = 'ICMP'
        self.parse()
    
    def parse(self):
        AbstractPacket.addMsg(AbstractPacket, 'Started Parsing ICMP packet')
        binUdpHeader = self.binPacket[self.headerMargin:self.headerMargin + self.ICMP_HEADER_LENGTH]
        unpackedHeader = unpack(self.UNPACK_FORMAT, binUdpHeader)
        self.icmpType = str(unpackedHeader[0])
        self.icmpCode = str(unpackedHeader[1])
        self.icmpCheckSum = unpackedHeader[2]
             
        fullHeaderSize = self.headerMargin + self.ICMP_HEADER_LENGTH
        self.dataSize = len(self.binPacket) - fullHeaderSize
            # get data from the packet
        self.data = self.binPacket[fullHeaderSize:]
        AbstractPacket.addMsg(AbstractPacket, 'Parsed ICMP  packet from port of type '+ self.icmpType)
        AbstractPacket.addMsg(AbstractPacket, 'ICMP-PACKET data:\n\n\n ' + str(self.data) +'\n\n')

    def getMsg(self):
        return self.msg
    
    def getName(self):
        return self.PROTOCOL_NAME
    
    def __del__(self):
        pass