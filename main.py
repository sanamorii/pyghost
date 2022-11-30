from sqlite3 import Error
from blake3 import blake3
import os
import sqlite3

FIND_ID_BY_HASH = """SELECT file_id 
FROM index 
WHERE file_hash = ?"""

class Database(object):
    def __init__(self, location=None):
        if location == None:
            self.conn = sqlite3.connect(location)
        else:
            self.conn = sqlite3.connect(":memory:")
        self.curs = self.conn.cursor()

    def conditionalupdate(self, query):
        result = self.curs.execute(FIND_ID_BY_HASH,(hash,)).fetchall()
        if result:
            pass
        else:
            try:
                self.curs.execute(query,())
            except Exception as e:
                print(e)

    def createtable(self, query):
        try:
            self.curs.execute(query)
        except Error as e:
            print(e)

    def executequery(self, query, values):
        self.curs.executemany(query, values)
    
    def initialize(self):
        CREATE_INDEX_TABLE = """CREATE TABLE "index" (
        "file_id"	INTEGER NOT NULL UNIQUE,
        "file_name"	TEXT NOT NULL,
        "file_dir"	TEXT NOT NULL,
        "file_hash"	TEXT NOT NULL,
        PRIMARY KEY("file_id" AUTOINCREMENT)
        )"""
        self.createtable(query=CREATE_INDEX_TABLE)



def Hash(file):
    BUFFER = 65536

    hasher = blake3()

    with open(file, "rb") as f:
        while True:
            data = f.read(BUFFER)
            if not data:
                break
            hasher.update(data)
    
    return hasher.hexdigest()


def Crawl():
    dbhandler = Database(location="./filedb.db")
    dbhandler.initialize()

    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            hash = Hash(file=path)
            
    
