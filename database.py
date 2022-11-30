import sqlite3
from sqlite3 import Error

# def CreateConn(dbFile):

#     conn = None
#     try:
#         conn = sqlite3.connect(dbFile)  # physcal
#         conn = sqlite3.connect(':memory:')  # memory
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()
    
# if __name__ == "__main__":
#     CreateConn(r"./db/test.db")

def CreateConn(dbFile):

    conn = None
    try:
        # conn = sqlite3.connect(dbFile)  # physcal
        conn = sqlite3.connect(':memory:')  # memory
        
    except Error as e:
        print(e)
    
    return conn
    
def CreateTable(conn, query: str):
    try:
        curs = conn.cursor()
        curs.execute(query)
    except Error as e:
        print(e)

# st_query = '''CREATE TABLE "dupe_files" (
# 	"file_id"	INTEGER NOT NULL UNIQUE,
# 	"file_name"	TEXT NOT NULL,
# 	"file_location"	TEXT NOT NULL,
# 	"file_md5"	TEXT NOT NULL,
# 	"file_sha1"	TEXT NOT NULL,
# 	PRIMARY KEY("file_id" AUTOINCREMENT)
# )'''

CREATE_INDEX_TABLE = '''CREATE TABLE "file_index" (
	"file_id"	INTEGER NOT NULL UNIQUE,
	"file_name"	TEXT NOT NULL,
	"file_dir"	TEXT NOT NULL,
	"file_sha256"	TEXT NOT NULL,
	PRIMARY KEY("file_id" AUTOINCREMENT)
)'''

CREATE_DUPLICATE_TABLE = '''CREATE TABLE "file_duplicates" (
	"entry_id"	INTEGER NOT NULL UNIQUE,
	"file_id"	INTEGER NOT NULL,
	"file_name"	TEXT NOT NULL,
	"file_dir"	TEXT NOT NULL,
	PRIMARY KEY("entry_id" AUTOINCREMENT),
	FOREIGN KEY("file_id") REFERENCES "file_index"("file_id")
)'''

if __name__ == "__main__":
    CreateConn(r"./db/test.db")

