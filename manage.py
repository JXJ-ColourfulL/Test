from flask_migrate import MigrateCommand
from flask_script import Manager

from FlaskTpp import create_app

app = create_app("develop")

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
