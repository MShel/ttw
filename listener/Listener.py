import socket
import subprocess
import netifaces
from datetime import datetime
from pprint import pprint
import json
import threading
from struct import unpack
from listener.packets.ipPacket import IpPacket 
from listener.packets.packetFactory import PacketFactory
from listener.packets.abstractPacket import AbstractPacket
from stats.sessionData import SessionData

class Listener:
    
    ETHERNET_HEADER_LENGTH = 14
    ETHERNET_UNPACK_HEADER = '!6s6sH'
    BUFFER_SIZE = 65565
    
    
    def __init__(self, protocol='all', verbose=False,):
        self.logger = None
        self.protocols = [['tcp', 6], ['udp', 17], ['icmp', 1], ['all', 0]]
        self.startDateTime = datetime.now();
        self.setVerbose(verbose)
        self.setProtocol(protocol)
        self.protocolIndex = list(filter(lambda pr: pr[0] == self.getProtocol(), self.protocols))[0][1]
        self.sessionData = SessionData()
        # self.interfaces = self.getInterfaces()
        # self.getAllConnections()
        
    def getAllConnections(self):
        # self.indexInterface = input('Select an interface - number from 0 to ' + str(len(self.interfaces) - 1) + '^')
        pass
    
    def getInterfaces(self) -> list:
        networkInterfaces = netifaces.interfaces()
        
        for i in range(len(networkInterfaces)):
            print(str(i) + ' - ' + networkInterfaces[i])
        return networkInterfaces
    
    '''
    gets the stream creats Packets, parses and saves them if needed
    '''  
    def getPartyStarted(self):
  
        allConnectionsSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        print(self.startDateTime.strftime('Started Listening at - %H:%M:%S:%f | %b %d %Y'))
        # receive a packet
        while True:
            binPacket, sendersInfo = allConnectionsSocket.recvfrom(self.BUFFER_SIZE)
            # networkAdapter = sendersAddressInfo[0]
     
            ethernetHeader = binPacket[:self.ETHERNET_HEADER_LENGTH]
            unpackedEthernetHeader = unpack(self.ETHERNET_UNPACK_HEADER , ethernetHeader)
            transportProtocol = socket.ntohs(unpackedEthernetHeader[2])
            # only ip stuff is supported for now
            if(transportProtocol == 8):
                ipObj = IpPacket(binPacket, self.ETHERNET_HEADER_LENGTH)
                if self.getVerbose() == True: print(ipObj.getMsg())
                
                if (self.getProtocol() == 'all' or self.protocolIndex == ipObj.protocol):
                    ipChildPacketBinMargin = ipObj.iphLength + self.ETHERNET_HEADER_LENGTH
                    packetObj = PacketFactory.factory(ipObj.protocol, binPacket, ipChildPacketBinMargin)
                    if self.getVerbose() == True: print(packetObj.getMsg())
                    if self.getLogger() != None:  packetObj.writeToLog(self.getLogger(), self.getLogFormat())
                    self.sessionData.addPacket(ipObj, packetObj)
    
    def printStatistic(self):
        endTime = datetime.now()
        print(endTime.strftime('Finished Listening at - %H:%M:%S:%f | %b %d %Y'))
        print('Listened for ' + str(endTime - self.startDateTime))
        print(self.sessionData.jsonify())
        # print(str(self.parsedPacketsCounter).ljust(4) + ' total packets')
        # print(str(self.parsedPacketsCounter).ljust(4) + ' packetType packages')
        # print(str(self.parsedPacketsCounter) + ' to {address}')
        
        
           
    def getPort(self):
        return self.port
    def setPort(self, port):
        self.port = port
    
    def getVerbose(self):
        return self.verbose
    def setVerbose(self, verbose):
        self.verbose = verbose
    
    def getProtocol(self):
        return self.protocol
    def setProtocol(self, protocol):
        self.protocol = str.lower(protocol)      
    
    def getLogger(self):
        return self.logger
    def setLogger(self, logger):
        self.logger = logger
        return self
