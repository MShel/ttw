from listener.packets.abstractPacket import AbstractPacket
from struct import unpack

class UdpPacket(AbstractPacket):
    
    UNPACK_FORMAT = '!HHHH'
    UDP_HEADER_LENGTH = 8
    PROTOCOL_NAME = 'UDP'
    
    def __init__(self, binPacket: bytes, margin: int):
        self.binPacket = binPacket
        self.headerMargin = margin
        self.parse()
    
    def parse(self):
        AbstractPacket.addMsg(AbstractPacket, 'Started Parsing UDP packet')
        binUdpHeader = self.binPacket[self.headerMargin:self.headerMargin + self.UDP_HEADER_LENGTH]
        unpackedHeader = unpack(self.UNPACK_FORMAT, binUdpHeader)
        self.fromPort = str(unpackedHeader[0])
        self.toPort = str(unpackedHeader[1])
        self.udpHeaderLength = unpackedHeader[2]
        self.udpCheckSum = unpackedHeader[3]
             
        fullHeaderSize = self.headerMargin + self.udpHeaderLength
        self.dataSize = len(self.binPacket) - fullHeaderSize
            # get data from the packet
        self.data = self.binPacket[fullHeaderSize:]
        AbstractPacket.addMsg(AbstractPacket, 'Parsed UDP  packet from port: ' + self.fromPort + ' to: ' + self.toPort)
        AbstractPacket.addMsg(AbstractPacket, 'UDP-PACKET data:\n\n\n ' + str(self.data) +'\n\n')

    def getMsg(self):
        return self.msg
    
    def getName(self):
        return self.PROTOCOL_NAME
    
    def __del__(self):
        pass