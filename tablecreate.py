import psycopg2 as pg
class Pet:
    def __init__(self,pid,owner_name,pet_name,p_type,p_breed):
        self.pid=pid
        self.owner_name=owner_name
        self.pet_name=pet_name
        self.p_type=p_type
        self.p_breed=p_breed

class DBConnection():
    conn=None
    cur=None
    def __init__(self):
        pass

    @classmethod
    def connect_db(cls):
        cls.conn=pg.connect('dbname=postgres user=postgres password=Finserv@2023')
        cls.cur=cls.conn.cursor()


    @classmethod
    def create_table(self,tablename,f1,f2,f3,):
        self.cur.execute('DROP TABLE IF EXISTS ' + str(tablename))
        self.cur.execute('CREATE TABLE '+ str(tablename)+'(id serial PRIMARY KEY,' + str(f1)+ ' varchar (20) NOT NULL,' + str(f2) + ' varchar (20) NOT NULL,' + str(f3) + ' varchar(20) NOT NULL);')
        self.conn.commit()


    @classmethod
    def insert_db(self,tablename,f1,f2,f3):
        self.cur.execute('INSERT INTO '+ str(tablename)+ ' (pet_name,p_breed,owner_name) VALUES(%s, %s, %s);',(str(f1),str(f2),str(f3)))
        self.conn.commit()
    

    @classmethod
    def select_read(self,tablename):
        self.cur.execute('SELECT * FROM '+str(tablename)+';')
        return self.cur.fetchall()

    @classmethod
    def delete_row(self,tablename,ids):
        self.cur.execute('DELETE FROM '+str(tablename)+' Where pid = %s;',(ids,))
        self.conn.commit()

    @classmethod
    def edit(self,tablename,f1,f2,f3,ids):
        self.cur.execute("UPDATE "+str(tablename)+ " SET pet_name = '" + str(f1) + "',p_breed = '" + str(f2) + "',owner_name = '" + str(f3) + "' WHERE pid = %s;",(ids,))   
        self.conn.commit()

    @classmethod
    def close(self):
        self.cur.close()
        self.conn.close()





    

