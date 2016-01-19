from stats.factories.abstractFactory import AbstractFactory
from stats.adapters.abstractAdapter import AbstractAdapter
from stats.adapters.sqliteAdapter import SqliteAdapter
from stats.adapters.mysqlAdapter import MysqlAdapter


class SqlFactory(AbstractFactory):
    
    # schema - sql database structure, json - mongoDb, etc
    schema = ''
    
   
    @staticmethod
    def factory(factoryType: str, credentials: object) -> AbstractAdapter:
        adapter = None
        if factoryType == 'sqlite' : adapter = SqliteAdapter(credentials)
        elif factoryType == 'mysql' : adapter = MysqlAdapter(credentials)
        SqlFactory.buildSchema(adapter)
        return adapter
    
    @staticmethod
    def buildSchema(adapter: AbstractAdapter):
        try:
            adapter.executeSchema()
        except Exception as e:
            #do nothing we already have schema
            pass
             
