def get_sqlalchemy_uri(DATABASE):
    dialect = DATABASE.get('dialect')
    driver = DATABASE.get('driver')
    username = DATABASE.get('username')
    password = DATABASE.get('password')
    host = DATABASE.get('host')
    port = DATABASE.get('port')
    database = DATABASE.get('database')
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,driver,username,password,host,port,database)



class Config():
    Debug = False
    Test = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SESSION_KEY = 'djkadl'
    CERATER_TYPE = 'mysql'



class DevelopConfig(Config):
    Debug = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'root',
        'password': '123456',
        'host': 'localhost',
        'port': '3306',
        'database': 'CloudHosting'
    }
    SQLALCHEMY_DATABASE_URI = get_sqlalchemy_uri(DATABASE)



NEV_NAME={
    'develop': DevelopConfig
}