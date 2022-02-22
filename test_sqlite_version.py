import sqlite3
import sys


print(sqlite3.sqlite_verion)


if sqlite3.sqlite_version_info < (3, 9, 0):
    sys.exit(1)
