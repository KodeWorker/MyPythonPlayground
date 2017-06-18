import MySQLdb

def Main():
    try:
        con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='test')
        cur = con.cursor()
        
#        cur.execute('SELECT version()')
#        cur.execute('DROP TABLE Pets')
        cur.execute("""
                    DROP TABLE IF EXISTS Pets;
                    CREATE TABLE Pets(Id INT, Name TEXT, Price INT);
                    INSERT INTO Pets VALUES(1, "Cat", 400);
                    INSERT INTO Pets VALUES(2, "Dog", 600);
                    """)
        
        pets =((3, "Rabbit", 200),
               (4, "Bird", 60),
               (5, "Goat", 500))

        cur.executemany('INSERT INTO Pets VALUES(%s, %s, %s)', pets)
        
#        cur.execute('CREATE TABLE Pets(Id INT, Name TEXT, Price INT)')        
#        cur.execute('INSERT INTO Pets VALUES(1, "Cat", 400)')
#        cur.execute('INSERT INTO Pets VALUES(2, "Dog", 600)')
#        cur.execute('INSERT INTO Pets VALUES(3, "Rabbit", 200)')
#        cur.execute('INSERT INTO Pets VALUES(4, "Bird", 60)')
        cur.close()
        con.commit()
#
        cur = con.cursor()
        cur.execute('SELECT * FROM Pets')
        data = cur.fetchall()        
        cur.close()
        
        for row in data:
            print(row)
        
    except MySQLdb.Error:
        if con:
            print('Error! Rolling back!')
            con.rollback()                
    finally:
       if con:
           con.close()

if __name__ == '__main__':
    Main()