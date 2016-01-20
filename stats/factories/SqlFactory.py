from stats.factories.abstractFactory import AbstractFactory
from stats.adapters.abstractAdapter import AbstractAdapter
from stats.adapters.sqliteAdapter import SqliteAdapter
from stats.adapters.mysqlAdapter import MysqlAdapter
import sqlite3
from stats.adapters.NullAdapter import NullAdapter

class SqlFactory(AbstractFactory):
    
    # schema - sql database structure, json - mongoDb, etc
    schema = ''
    
   
    @staticmethod
    def factory(adapterType: str, credentials: dict) -> AbstractAdapter:
        adapter = NullAdapter(credentials)
        if adapterType == 'sqlite' : adapter = SqliteAdapter(credentials)
        elif adapterType == 'mysql' : adapter = MysqlAdapter(credentials)
        SqlFactory.buildSchema(adapter)
        return adapter
    
    @staticmethod
    def buildSchema(adapter: AbstractAdapter):
        try:
            adapter.executeSchema()
        except sqlite3.OperationalError as e:
            if str(e).find('already exists') != -1 :
                #do nothing we already have schema
                pass
            else:
                print(e) 
