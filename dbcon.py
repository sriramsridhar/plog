import peewee as pw

myDB = pw.MySQLDatabase("plog", host="localhost", user="root", passwd="svss1995")


class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB


class User(MySQLModel):
    username = pw.CharField()
    password = pw.CharField()
    # etc, etc
    class Meta:
        order_by = ('username',)

class Log(MySQLModel):
    time = pw.DateTimeField()
    log_type = pw.CharField()
    log_content = pw.TextField()
    rating = pw.IntegerField()
    log_user = pw.CharField()

# when you're ready to start querying, remember to connect
myDB.connect()
myDB.create_tables([User, Log], safe=True)
