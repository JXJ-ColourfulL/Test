ADMIN_USER_TOKEN_CACHE_TIME = 60*60*24*7
CINEMA_USER_TOKEN_CACHE_TIME = 60*60*24*7


class Config():
    DEBUG = False
    Testing = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_db_uri(DATABASE):
    dialct = DATABASE.get("dialct")
    driver = DATABASE.get("driver")
    username = DATABASE.get("username")
    passwd = DATABASE.get("passwd")
    port = DATABASE.get("port")
    host = DATABASE.get("host")
    database = DATABASE.get("database")
    return "{}+{}://{}:{}@{}:{}/{}".format(dialct, driver, username, passwd, port, host, database)


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        "dialct": "mysql",
        "driver": 'pymysql',
        "username": "root",
        "passwd": "123456",
        "port": "106.14.2.56",
        "host": "3306",
        "database": "Tpp"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)



ENV = {
    'develop': DevelopConfig
}