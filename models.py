import sqlite3 as sql

def insert_user(usr,psw,type):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO userDetails (userName,password,userType) VALUES (?,?,?)", (usr,psw,type,))
    con.commit()
    con.close()
	
def select_user():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("select userName,password from userDetails")
	result = cur.fetchall()
	con.close()
	return result
 
    # def insert_contact(name,phone,username,email):
        # con = sql.connect("database.db")
        # cur = con.cursor()
        # cur.execute("INSERT INTO contact (name,phone,username,email) VALUES (?,?,?,?)", (name,phone,username,email))
        # con.commit()
        # con.close()

    # def select_account_holder(params=()):
        # con = sql.connect("database.db")
        # cur = con.cursor()
        # if params==():
            # cur.execute("select * from account_holder")
        # else:
            # string = "select"
            # for i in xrange(len(params)-1):
                # string += "%s,"
            # string += "%s"
            # string += " from account_holder"

            # result = cur.execute(string)
            # con.close()
            # return result.fetchall()

    # def select_contact(params=()):
        # con = sql.connect("database.db")
        # cur = con.cursor()
        # if params==():
            # cur.execute("select * from contact")
        # else:
            # string = "select"
            # for i in xrange(len(params)-1):
                # string += "%s,"
            # string += "%s"
            # string += " from contact"

            # result = cur.execute(string)
            # con.close()
            # return result.fetchall()