from configparser import ConfigParser
import pymysql

from ini import db

class DBCrudInstantiator:

    use_db = 'local_test'

    def __init__(self, user_query):
        self.config = ConfigParser()
        self.user_query = user_query

    @classmethod
    def make_mysqldb_connection(self, config, cls, user_query):
        config.read(db.ini)
        test_config = config[cls.use_db]

        test_db = pymysql.connect(
            host=test_config['hostname'],
            port=int(test_config['port']),
            user=test_config['user'],
            passwd=test_config['password'],
            db=test_config['db'],
            local_infile = 1
        )
        try:
            with test_db.cursor() as cursor:
                cursor.execute(user_query)
                test_db.commit()

        except Exception as e:
            print(f'Encountered error when executing MySQL query: \n{e}')

        finally:
            test_db.close()
