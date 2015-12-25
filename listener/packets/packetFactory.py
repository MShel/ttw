from listener.packets.othersPacket import OthersPacket
from listener.packets.tcpPacket import TcpPacket
from listener.packets.udpPacket import UdpPacket
from listener.packets.icmpPacket import IcmpPacket
from listener.packets.abstractPacket import AbstractPacket

class PacketFactory:
    def factory(packetType: int, binPacket: bytes, margin) -> AbstractPacket:
        packet = None

        # try:
        if packetType == 6 : packet = TcpPacket(binPacket, margin)
        elif packetType == 17 : packet = UdpPacket(binPacket, margin)
        elif packetType == 1 : packet = IcmpPacket(binPacket, margin)
      
        if packet == None: packet = OthersPacket(binPacket, margin)
            
        # except Exception:
            # figure out the way to let meaningfullExcaption bubble up
         #   pass
        return packet    
    factory = staticmethod(factory)
