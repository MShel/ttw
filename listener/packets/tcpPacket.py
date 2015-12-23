from listener.packets.abstractPacket import AbstractPacket
from struct import unpack

class TcpPacket(AbstractPacket):
    
    UNPACK_FORMAT = '!HHLLBBHHH'
    TCP_HEADER_LENGTH = 20
    
    def __init__(self, binPacket, margin):
        self.binPacket = binPacket
        self.headerMargin = margin
        self.status = self.STATUS_INITIATED
        self.parse()
    
    def parse(self):
        AbstractPacket.addMsg(AbstractPacket, 'Started Parsing TCP packet')
        binTcpHeader = self.binPacket[self.margin:self.margin + 20]
        unpackedHeader = unpack(self.UNPACK_FORMAT, binTcpHeader)
        self.fromPort = unpackedHeader[0]
        self.toPort = unpackedHeader[1]
        self.sequence = unpackedHeader[2]
        self.acknowledgement = unpackedHeader[3]
        self.doffReserved = unpackedHeader[4]
        self.tcpHeaderLength = self.doff_reserved >> 4
             
             
        fullHeaderSize = self.headerMargin + self.tcpHeaderLength * 4
        self.dataSize = len(self.binPacket) - fullHeaderSize
            #get data from the packet
        self.data = self.binPacket[fullHeaderSize:]
        AbstractPacket.addMsg(AbstractPacket, 'Parsed TCP packet from port: ' + self.fromPort + ' to: ' + self.toPort)

    def getMsg(self):
        return self.msg
    
    def __del__(self):
        pass
    
