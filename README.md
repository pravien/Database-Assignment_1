# Database-Assignment_1

This repo contain 3 files 

The first file is simple_db.py. This is the library we are going to use to read and write to a file.

The second file is simple_db_writer.py. This file contains an example that shows how to write key value pairs to a file.

The third file is simple_db_reader.py. This file contains an example that shows how to read to read key value pairs from a file.



# How to use the class

### If you have python installed:


1. Clone the repo to your computer. 

2. create a file called database.txt in the repo. This is a must!!!

3. Run file simple_db_writer.py first by using the command : 

```    
python simple_db_writer.py
```
- This script will populate the file database.txt with some key value pairs.

    
4. After this run the script called simple_db_reader.py using command:
```    
python simple_db_reader.py
```

5. this script will read all the key value pairs from the file database.txt. It will produce the following output :
```    
annas 5
banana 8
cranberry 4909
```

### If you don't have python installed:

If you don'y python installed you can use docker.

1. Fork the repo to your computer. 

2. create a file called database.txt in the repo.

3. Run the following docker command : 

```    
docker run -it --rm -v $(pwd):/src -w /src helgecph/pythonruby sh -c "python simple_db_writer.py;python simple_db_reader.py"
```

