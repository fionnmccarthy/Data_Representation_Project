import mysql.connector
import db_config as cfg
import datetime

class lunchDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    

    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']


    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor


    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    # creates a lunch order for student
    def create(self, values):

       cursor = self.getcursor()
       sql="insert into lunches (lunch_option, student_id, dttm) values (%s,%s,%s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.closeAll()
       return newid
        
    #counts number ordered of each lunch
    def countchoices(self, lunch_option):
        
        cursor = self.getcursor()
        sql="select count(*) as total from lunches where lunch_option like %s"
        values = (lunch_option,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        name = result[0]
        
        self.closeAll()
        return name

    #deletes orders made
    def delete_entries(self):
        
        cursor = self.getcursor()
        sql="delete * from lunches"
        cursor.execute(sql)

        self.closeAll()     


    def convertToDictionary(self, result):
        pass
    '''
        colnames=['id','title','author', "price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
       '''


    def createtable(self):
        cursor = self.getcursor()
        sql="create table lunches (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, lunch_option varchar(250), student_id varchar(20), dttm datetime)"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()


    def createdatabase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql="create database "+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()

    def insert_data(self):
        cursor = self.getcursor()
        now = datetime.datetime.now()
        data = ('Chicken Salad', 'G000000', now)
        data2 = ('Soup and Bread', 'G000001', now)
        data3 = ('Chicken Salad', 'G000002', now)
        data4 = ('Soup and Bread', 'G000003', now)
        data5 = ('Vegtable Rizotto', 'G000004', now)
        data6 = ('Chicken Salad', 'G000005', now)
        data7 = ('Tuna Melt', 'G000006', now)
        data8 = ('Chicken Salad', 'G000007', now)
        data9 = ('Chorizo Pasta', 'G000008', now)
        lunchDAO.create(data)
        lunchDAO.create(data2)
        lunchDAO.create(data3)
        lunchDAO.create(data4)
        lunchDAO.create(data5)
        lunchDAO.create(data6)
        lunchDAO.create(data7)
        lunchDAO.create(data8)
        lunchDAO.create(data9)
       

lunchDAO = lunchDAO()

if __name__ == "__main__":
    #lunchDAO.createdatabase()
    #lunchDAO.createtable()
    lunchDAO.insert_data()
    now = datetime.datetime(2009, 5, 5)
    data = ('Chicken Salad', 'D12345', now)
    lunchDAO.create(data)
    counted_choices = lunchDAO.countchoices('Chicken Salad')
    print (counted_choices)

    print("sanity")