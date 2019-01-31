import sys
class simple_db:

    def __init__(self, filename):
        self.filename = filename
        self.last_b = 0
        self.dict = self.create_dict(filename)

    def create_dict(self,filename):
        try:
            key = ""
            my_dict={}
            key_not_found = True
            with open(filename, 'r') as f:
                while(True):
                    c = f.read(1)
                    if not c:
                        break
                    if c is ":":
                        key_not_found = False
                        my_dict[key] = f.tell()
                        key = ""
                    elif c != ":" and key_not_found:
                        key+=c

                    elif c is "\n":
                        key_not_found = True
                f.readline()
                self.last_b = f.tell()
            return my_dict
        except FileNotFoundError as e:
            print("File not Found")
            sys.exit()

    def db_write(self,key,value):
        key = str(key)
        value = str(value)+"\n"

        str_ = key+":"+value
        str_len = len(str_.split(":")[0])
        offset = len(key)+1
        offset = self.last_b+offset

        with open(self.filename, 'a+') as f:
            f.write(str_)
        self.dict[key] = offset
        temp = offset+len(value)
        self.last_b = offset+len(value)

    def db_read(self,key):
        with open(self.filename, 'r+') as f:
            f.seek(self.dict[str(key)])
            return f.readline().replace("\n","")

    def get_each_pair(self):
        my_list = [(key,self.db_read(key))for key in self.dict.keys()]
        return my_list

if __name__ == '__main__':

    #k = simple_db("database.txt")
    #k.db_write("annas","3")
    #k.db_write("banana","8")
    #k.db_write("cranberry","4909")
    #k.db_write("annas","5")
    #print(k.db_read("annas"))
    #print(k.db_read("banana"))
    #print(k.db_read("cranberry"))
    #k.get_each_pair()
    print("hey")
