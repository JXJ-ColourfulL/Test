from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    Id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    U_name = db.Column(db.String(16),unique=True)
    U_pwd = db.Column(db.String(128))
    U_email = db.Column(db.String(64),unique=True)
    U_phone = db.Column(db.String(11),unique=True)


class Host(db.Model):
    Id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Disk_space = db.Column(db.Integer)
    Monthly_data_transfer = db.Column(db.Integer)
    FTP_accounts = db.Column(db.Integer)
    Email_boxes = db.Column(db.Integer)
    Free_domains = db.Column(db.Integer)


class Configuration(db.Model):
    Id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    C_account = db.Column(db.String(64))
    C_password = db.Column(db.String(16))
    C_system = db.Column(db.String(64))
    C_ip = db.Column(db.String(32),unique=True)

class Order(db.Model):
    Id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    U_id = db.Column(db.ForeignKey(User.Id))
    C_id = db.Column(db.ForeignKey(Configuration.Id))
    H_id = db.Column(db.ForeignKey(Host.Id))


