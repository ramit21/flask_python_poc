from peewee import *
import datetime

db = SqliteDatabase('posts.db') # a file named posts.db will be created

class Post(Model):
    id = PrimaryKeyField()
    date = DateTimeField(default = datetime.datetime.now)
    title = CharField()
    text = TextField() # long string

    class Meta:
        database = db #Db object for this entity
        
def intialize_db():
    db.connect()
    db.create_tables([Post], safe=True)