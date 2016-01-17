from stats.factories.abstractFactory import AbstractFactory
from stats.adapters.abstractAdapter import AbstractAdapter
from stats.adapters.sqliteAdapter import SqliteAdapter
from stats.adapters.mysqlAdapter import MysqlAdapter


class SqlFactory(AbstractFactory):
    
    # schema - sql database structure, json - mongoDb, etc
    schema = ''
    
   
    @staticmethod
    def factory(factoryType: str, credentials: dict) -> AbstractAdapter:
        adapter = None
        if factoryType == 'sqlite' : adapter = SqliteAdapter(credentials)
        elif factoryType == 'mysql' : adapter = MysqlAdapter(credentials)
        SqlFactory.buildSchema(adapter,adapter.getSchema())
        return adapter
    
    @staticmethod
    def buildSchema(adapter: AbstractAdapter, schema: str):
        pass 
