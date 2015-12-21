import socket
import subprocess
import netifaces
import sys,getopt
from datetime import datetime
import pprint
import json
from struct import *

def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b

class Listener:
    def __init__(self,protocol='all', verbose = False):
        self.setVerbose(verbose)
        self.setProtocol(protocol)
        self.interfaces = self.getInterfaces()
        self.getAllConnections()
        
    def getAllConnections(self):
        indexInterface = raw_input('Select an interface - number from 0 to '+str(len(self.interfaces)-1) + '^')
        pass
    
    def getInterfaces(self):
        networkInterfaces = netifaces.interfaces()
        
        for i in range(len(networkInterfaces)):
            print str(i) + ' - ' + networkInterfaces[i]
        return networkInterfaces
    
    def getStream(self):
        #tcpSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0006))
        #udpSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0017))
        #icmpSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0001))
        allSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
       
        # receive a packet
        while True:
            packet = allSocket.recvfrom(65565)
            '''
            initiate protocols protocol.{protocol}Protocol
            parse will happen from the obj
            '''
            #packet string from tuple
            packet = packet[0]
     
            #parse ethernet header
            eth_length = 14
     
            eth_header = packet[:eth_length]
            eth = unpack('!6s6sH' , eth_header)
            eth_protocol = socket.ntohs(eth[2])
            print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)
 
            #Parse IP packets, IP Protocol number = 8
            if eth_protocol == 8 :
                #Parse IP header
                #take first 20 characters for the ip header
                ip_header = packet[eth_length:20+eth_length]
         
                #now unpack them :)
                iph = unpack('!BBHHHBBH4s4s' , ip_header)
                version_ihl = iph[0]
                version = version_ihl >> 4
                ihl = version_ihl & 0xF
 
                iph_length = ihl * 4
                ttl = iph[5]
                protocol = iph[6]
                s_addr = socket.inet_ntoa(iph[8]);
                d_addr = socket.inet_ntoa(iph[9]);
                print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
                #TCP protocol
                if protocol == 6 :
                    t = iph_length + eth_length
                    tcp_header = packet[t:t+20]
                    #now unpack them :)
                    tcph = unpack('!HHLLBBHHH' , tcp_header)
                    source_port = tcph[0]
                    dest_port = tcph[1]
                    sequence = tcph[2]
                    acknowledgement = tcph[3]
                    doff_reserved = tcph[4]
                    tcph_length = doff_reserved >> 4
                    print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
                    h_size = eth_length + iph_length + tcph_length * 4
                    data_size = len(packet) - h_size
                    #get data from the packet
                    data = packet[h_size:]
                    print 'Data : ' + data
                #ICMP Packets
                elif protocol == 1 :
                    u = iph_length + eth_length
                    icmph_length = 4
                    icmp_header = packet[u:u+4]
                    #now unpack them :)
                    icmph = unpack('!BBH' , icmp_header)
                    icmp_type = icmph[0]
                    code = icmph[1]
                    checksum = icmph[2]
                    print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)
                    h_size = eth_length + iph_length + icmph_length
                    data_size = len(packet) - h_size
                    #get data from the packet
                    data = packet[h_size:]
                    print 'Data : ' + data
                #UDP packets
                elif protocol == 17 :
                    u = iph_length + eth_length
                    udph_length = 8
                    udp_header = packet[u:u+8]
                    #now unpack them :)
                    udph = unpack('!HHHH' , udp_header)
                    source_port = udph[0]
                    dest_port = udph[1]
                    length = udph[2]
                    checksum = udph[3]
                    print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum)
                    h_size = eth_length + iph_length + udph_length
                    data_size = len(packet) - h_size
                    #get data from the packet
                    data = packet[h_size:]
                    print 'Data : ' + data
                    #some other IP packet like IGMP
            else :
                print 'Protocol other than TCP/UDP/ICMP'
            print
    
    def getPort():
        return self.port
    
    def setPort(port):
        self.port = port
    
    def getVerbose():
        return self.verbose
    def setVerbose(self, verbose):
        self.verbose = verbose
    
    def getProtocol():
        return self.protocol
    def setProtocol(self, protocol):
        self.protocol = protocol               
