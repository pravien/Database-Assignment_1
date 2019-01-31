from simple_db import simple_db

database = simple_db("database.txt")
database.db_write("annas","3")
database.db_write("banana","8")
database.db_write("cranberry","4909")
database.db_write("annas","5")
