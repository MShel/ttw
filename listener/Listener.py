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
    def __init__(self, protocol='all', verbose=False,):
        self.logger = None
        self.protocols = [('tcp', 'udp', 'icmp'), ('8', '1', '23')]
        self.startDateTime = datetime.now();
        self.setVerbose(verbose)
        self.setProtocol(protocol)
        self.interfaces = self.getInterfaces()
        self.getAllConnections()
        
    def getAllConnections(self):
        self.indexInterface = raw_input('Select an interface - number from 0 to ' + str(len(self.interfaces) - 1) + '^')
        pass
    
    def getInterfaces(self):
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
            # parse ethernet header
            eth_length = 14
     
            eth_header = binPacket[:eth_length]
            eth = unpack('!6s6sH' , eth_header)
            eth_protocol = socket.ntohs(eth[2])
            if (self.getProtocol() == 'all' or self.protocols[self.getProtocol()] == eth_protocol):
                packetObj = PacketFactory.factory(eth_protocol, binPacket, self.getVerbose())
                if self.getVerbose() == True: print(packetObj.getMsg())
                if self.getLogger() != None:  packetObj.writeToLog(self.getLogger(), self.getLogFormat())
                self.parsedPacketsCounter += 1
                
    def printStatistic(self):
        endTime = datetime.now()
        print(endTime.strftime('Finished Listening at - %H:%M:%S:%f | %b %d %Y'))
        print('Listened for '+ str(endTime - self.startDateTime))
        print('Sent: ' )
        print(str(self.parsedPackets).ljust(4) + ' total packets')
        #print(str(self.parsedPackets).ljust(4) + ' packetType packages')
        #print(str(self.parsedPackets) + ' to {address}')
        
        
           
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
