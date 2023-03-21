"""Create Arango db connection for use within api routes"""
from pyArango.connection import *
from arango import ArangoClient
from .. config import settings

client = ArangoClient(hosts=settings.arango_host)

db = client.db(settings.arango_db, username=settings.arango_root_user,
               password=settings.arango_root_password)

colls = db.collections()

print(colls)
