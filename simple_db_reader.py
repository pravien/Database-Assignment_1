from simple_db import simple_db

database = simple_db("database.txt")
for key,val in database.get_each_pair():
    print(key,val)
