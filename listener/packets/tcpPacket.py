from listener.packets.abstractPacket import AbstractPacket
from struct import unpack

class TcpPacket(AbstractPacket):
    
    UNPACK_FORMAT = '!HHLLBBHHH'
    TCP_HEADER_LENGTH = 20
    PROTOCOL_NAME = 'TCP/IP'
    
    def __init__(self, binPacket: bytes, margin: int):
        self.binPacket = binPacket
        self.headerMargin = margin
        self.status = self.STATUS_INITIATED
        self.parse()
    
    def parse(self):
        AbstractPacket.addMsg(AbstractPacket, 'Started Parsing TCP packet')
        binTcpHeader = self.binPacket[self.headerMargin:self.headerMargin + self.TCP_HEADER_LENGTH]
        unpackedHeader = unpack(self.UNPACK_FORMAT, binTcpHeader)
        self.fromPort = str(unpackedHeader[0])
        self.toPort = str(unpackedHeader[1])
        self.sequence = unpackedHeader[2]
        self.acknowledgement = unpackedHeader[3]
        self.doffReserved = unpackedHeader[4]
        self.tcpHeaderLength = self.doffReserved >> 4
             
             
        fullHeaderSize = self.headerMargin + self.tcpHeaderLength * 4
        self.dataSize = len(self.binPacket) - fullHeaderSize
            # get data from the packet
        self.data = self.binPacket[fullHeaderSize:]
        AbstractPacket.addMsg(AbstractPacket, 'Parsed TCP  packet from port: ' + self.fromPort + ' to: ' + self.toPort)
        AbstractPacket.addMsg(AbstractPacket, 'TCP-PACKET data:\n\n\n ' + str(self.data) +'\n\n')

    def getMsg(self):
        return self.msg
    
    def getName(self):
        return self.PROTOCOL_NAME
    
    def __del__(self):
        pass
    


