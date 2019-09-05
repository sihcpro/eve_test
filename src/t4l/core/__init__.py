from eve import Eve
import logging

defaults = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'the_db_name',
    'DOMAIN': {'contacts': {}}
}

class ObjectServer(Eve):
    def __init__(self):
        super(ObjectServer, self).__init__(settings=defaults)
        logging.info(self.__module__)

        @self.route('/hello')
        def hello_world():
            return 'hello world!'


app = ObjectServer()


__all__ = ('app')
