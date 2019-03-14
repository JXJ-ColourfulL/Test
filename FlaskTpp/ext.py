from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 创建数据库实例
db = SQLAlchemy()
# 创建迁移实例
migrate = Migrate()

cache = Cache(config={'CACHE_TYPE': 'redis'})


def ext_init(app):
    # 初始化数据库
    db.init_app(app)
    # 初始化数据库迁移
    migrate.init_app(app=app, db=db)
    cache.init_app(app)
