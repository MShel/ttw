import socket
import subprocess
import netifaces
from datetime import datetime
import pprint
import json
import threading
from struct import *
from listener.packets.packetFactory import PacketFactory

class Listener:
    
    ETHERNET_HEADER_LENGTH = 14
    
    def __init__(self, protocol='all', verbose=False,):
        self.logger = None
        self.protocols = [['tcp', 6], ['udp', 17], ['icmp', 1]]
        self.startDateTime = datetime.now();
        self.setVerbose(verbose)
        self.setProtocol(protocol)
        self.protocolIndex = list(filter(lambda pr: pr[0] == self.getProtocol(), self.protocols))[0][1]
        #self.interfaces = self.getInterfaces()
        #self.getAllConnections()
        
    def getAllConnections(self):
        #self.indexInterface = input('Select an interface - number from 0 to ' + str(len(self.interfaces) - 1) + '^')
        pass
    
    def getInterfaces(self) ->list:
        networkInterfaces = netifaces.interfaces()
        
        for i in range(len(networkInterfaces)):
            print(str(i) + ' - ' + networkInterfaces[i])
        return networkInterfaces
    
    '''
    gets the stream creats Packets, parses and saves them if needed
    '''  
    def getPartyStarted(self):
  
        allConnectionsSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        self.parsedPacketsCounter = 0
        print(self.startDateTime.strftime('Started Listening at - %H:%M:%S:%f | %b %d %Y'))
        # receive a packet
        while True:
            binPacket, sendersAddressInfo = allConnectionsSocket.recvfrom(65565)
            

     
            eth_header = binPacket[:self.ETHERNET_HEADER_LENGTH]
            eth = unpack('!6s6sH' , eth_header)
            eth_protocol = socket.ntohs(eth[2])
            print(eth_protocol)
            print(binPacket)
            print(sendersAddressInfo)
            if (self.getProtocol() == 'all' or self.protocolIndex == eth_protocol):
                # packetObj = PacketFactory.factory(eth_protocol, binPacket, self.getVerbose())
                # if self.getVerbose() == True: print(packetObj.getMsg())
                # if self.getLogger() != None:  packetObj.writeToLog(self.getLogger(), self.getLogFormat())
                self.parsedPacketsCounter += 1
                
    def printStatistic(self):
        endTime = datetime.now()
        print(endTime.strftime('Finished Listening at - %H:%M:%S:%f | %b %d %Y'))
        print('Listened for ' + str(endTime - self.startDateTime))
        print('Sent: ')
        print(str(self.parsedPacketsCounter).ljust(4) + ' total packets')
        print(str(self.parsedPacketsCounter).ljust(4) + ' packetType packages')
        print(str(self.parsedPacketsCounter) + ' to {address}')
        
        
           
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
