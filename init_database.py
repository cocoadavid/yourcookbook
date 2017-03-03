from models import *


class InitDatabase:

    def init_db():
        ConnectDatabase.db.drop_tables([Food], safe=True)
        ConnectDatabase.db.create_tables([Food], safe=True)
