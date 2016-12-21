from thermos import app, db
from thermos.models import User
from flask.ext.script import Manager, prompt_bool

from thermos.models import User

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username='Username1', email='user1@example.com'))
    db.session.add(User(username='Username2', email='user2@example.com'))
    db.session.commit()
    print 'Initialized the database'


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to loose all your data"):
        db.drop_all()
        print 'Dropped the database'


if __name__ == '__main__':
    manager.run()
