import mysql.connector
import db_config as cfg
class membershipDAO:
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


    def create(self, values):
        cursor = self.getcursor()
        sql="insert into membership (Name, membership_type, email) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid


    def getAll(self):
        cursor = self.getcursor()
        sql="select * from membership"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray


    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from membership where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue


    def update(self, values):
        cursor = self.getcursor()
        sql="update membership set name= %s,membership_type=%s, email=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        

    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from membership where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        self.closeAll()
        
        print("delete done")


    def convertToDictionary(self, result):
        colnames=['id','Name','membership_type', "email"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item


    def insert_data(self):
        cursor = self.getcursor()
        data = ('John Doe', 'Gold', 'jd@live.ie')
        data2 = ('Jane Doe', 'Platinum', 'jd2@live.ie')
        data3 = ('John Snow', 'Silver', 'js@live.ie')
        data4 = ('Cian Doyle', 'Gold', 'cd@live.ie')
        data5 = ('Jack Connors', 'Silver', 'jc@live.ie')
        data6 = ('Sean McCarthy', 'Standard', 'smcc@live.ie')
        data7 = ('Neil Hassett', 'Standard', 'nh@live.ie')
        data8 = ('Laura Peters', 'Standard', 'lp@live.ie')
        data9 = ('Tom Moloney', 'Silver', 'tm@live.ie')
        data10 = ('Tom Clancy', 'Silver', 'tm@live.ie')
        data11 = ('Ciara Malone', 'Platinum', 'cm@live.ie')
        data12 = ('Sean Moloney', 'Standard', 'sm1234@live.ie')
        data13 = ('Pat Murphy', 'Standard', 'pm12@live.ie')
        data14 = ('Conor Downes', 'Gold', 'cd98@live.ie')

        membershipDAO.create(data)
        membershipDAO.create(data2)
        membershipDAO.create(data3)
        membershipDAO.create(data4)
        membershipDAO.create(data5)
        membershipDAO.create(data6)
        membershipDAO.create(data7)
        membershipDAO.create(data8)
        membershipDAO.create(data9)
        membershipDAO.create(data10)
        membershipDAO.create(data11)
        membershipDAO.create(data12)
        membershipDAO.create(data13)
        membershipDAO.create(data14)

    def createtable(self):
        cursor = self.getcursor()
        sql="create table membership (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, name varchar(250), membership_type varchar(50), email varchar(250))"
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


membershipDAO = membershipDAO()

if __name__ == "__main__":
    #membershipDAO.createdatabase()
    membershipDAO.createtable()
    membershipDAO.insert_data()
    data = ('Sarah Saunders', 'Gold', 'ss1995@live.ie')
    membershipDAO.create(data)
    #counted_choices = membershipDAO.countchoices('Chicken Salad')
    #print (counted_choices)

    print("sanity")