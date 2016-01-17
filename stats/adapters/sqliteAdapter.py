from listener.packets.abstractPacket import AbstractPacket
from pprint import pprint
import sqlite3

class SqliteAdapter:
    
    sqliteConnection = None
    
    schema = """CREATE TABLE `packet_stats` (
                     `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                     `toAddress` varchar(255) DEFAULT '',
                     `fromAddress` varchar(255) DEFAULT '',
                     `protocol` varchar(255) DEFAULT '',
                     `toPort` int(11) DEFAULT '0',
                     `fromPort`int(11) DEFAULT '0',
                     `created_at` datetime default current_timestamp
                     );
                CREATE TABLE `packet_data` (
                     `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                     `packet_id`int(11) DEFAULT '0',
                     `packet_data` BLOB DEFAULT '',
                     `created_at` datetime default current_timestamp
                );"""
    
    def __init__(self, credentials:dict):
        self.sqliteConnection = sqlite3.connect(credentials.databaseFilePAth)

    def recordPacket(self, packet:AbstractPacket):
        cursor = self.sqliteConnection.cursor()
        cursor.execute('INSERT INTO packet_stats VALUES (?,?,?,?,?)', (packet.toAddress, packet.fromAddress, packet.protocol, packet.toPort, packet.fromPort))
        cursor.commit()
        cursor.execute('INSERT INTO packet_data VALUES (?,?)', (cursor.lastrowid, packet.data))
        cursor.commit()
        return cursor.lastrowid
    
    def executeSchema(self,schema):
        self.sqliteConnection.cursor().execute(self.schema)
        self.sqliteConnection.cursor().commit