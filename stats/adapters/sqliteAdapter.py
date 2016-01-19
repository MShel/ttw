from listener.packets.abstractPacket import AbstractPacket
from pprint import pprint
import sqlite3

class SqliteAdapter:
    
    sqliteConnection = None
   
               
    
    def __init__(self, credentials:object):
        self.sqliteConnection = sqlite3.connect(credentials)
        self.schemas = ["""CREATE TABLE `packet_stats` (
                     `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                     `toAddress` varchar(255) DEFAULT '',
                     `fromAddress` varchar(255) DEFAULT '',
                     `protocol` varchar(255) DEFAULT '',
                     `toPort` int(11) DEFAULT '0',
                     `fromPort`int(11) DEFAULT '0',
                     `created_at` datetime default current_timestamp
                     );
                    """,""" CREATE TABLE `packet_data` (
                     `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                     `packet_id`int(11) DEFAULT '0',
                     `packet_data` TEXT DEFAULT '',
                     `created_at` datetime default current_timestamp
                    );"""]
        
    def recordPacket(self, packet:AbstractPacket):
        cursor = self.sqliteConnection.cursor()
        cursor.execute('INSERT INTO packet_stats(toAddress,fromAddress,protocol,toPort,fromPort) VALUES (?,?,?,?,?)', (packet.toAddress, packet.fromAddress, packet.protocol, packet.toPort, packet.fromPort))
        self.sqliteConnection.commit()
        cursor.execute('INSERT INTO packet_data(packet_id,packet_data) VALUES (?,?)', (cursor.lastrowid, packet.data))
        self.sqliteConnection.commit()
        return cursor.lastrowid
    
    def executeSchema(self):
        for schema in self.schemas:
            cursor = self.sqliteConnection.cursor()
            cursor.execute(schema)
            self.sqliteConnection.commit()