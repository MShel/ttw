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
    def __init__(self,protocol='all', verbose = False, ):
        self.logger = None
        self.setVerbose(verbose)
        self.setProtocol(protocol)
        self.interfaces = self.getInterfaces()
        self.getAllConnections()
        
    def getAllConnections(self):
        self.indexInterface = raw_input('Select an interface - number from 0 to '+str(len(self.interfaces)-1) + '^')
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
  
        allSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        parsedPackets = 0
        # receive a packet
        while True:
            binPacket, sendersAddressInfo = allSocket.recvfrom(65565)
            #parse ethernet header
            eth_length = 14
     
            eth_header = binPacket[:eth_length]
            eth = unpack('!6s6sH' , eth_header)
            eth_protocol = socket.ntohs(eth[2])
            if (self.getProtocol() == 'all' or self.procols[self.getProtocol()] == eth_protocol):
                packetObj = PacketFactory.factory(eth_protocol,binPacket,self.getVerbose())
                if self.getVerbose() == True: print(packetObj.getMsg())
                if self.getLogger() != None:  packetObj.writeToLog(self.getLogger(), self.getLogFormat())
                parsedPackets+=1
                
    def getPort(self):
        return self.port
    
    def setPort(self,port):
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
    def setLogger(self,logger):
        self.logger = logger
        return self
