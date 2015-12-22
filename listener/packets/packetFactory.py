from listener.packets.othersPacket import OthersPacket
from listener.packets.tcpPacket import TcpPacket
from listener.packets.udpPacket import UdpPacket
from listener.packets.icmpPacket import IcmpPacket
from listener.packets.abstractPacket import AbstractPacket

class PacketFactory:
    def factory(packetType: int, binPacket, verbose = True) -> AbstractPacket:
        packet = None
        try:
            if packetType == 'tcp' : packet = TcpPacket(binPacket)
            elif packetType == 'udp' : packet = UdpPacket(binPacket)
            elif packetType == 'icmp' : packet = IcmpPacket(binPacket)
            if packet == None: packet = OthersPacket(binPacket)
            
            packet.setVerbose(verbose)
        except Exception:
            #figure out the way to let meaningfullExcaption bubble up
            pass
        return packet    
    factory = staticmethod(factory)
