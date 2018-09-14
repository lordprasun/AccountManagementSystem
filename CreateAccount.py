import pymysql
def createAccount(AccountDetails):
    try:
        count = 1
        FirstName = AccountDetails["FirstName"]
        LastName = AccountDetails["LastName"]
        Name = (FirstName + LastName).upper()
        DateOfBirth = AccountDetails["DateOfBirth"]
        Address = AccountDetails["Address"]
        Email = AccountDetails["Email"]
        ContactNo= AccountDetails["ContactNo"]
        AccountNo = Name[:4]+ DateOfBirth + ("{:05d}".format(count))
        connection =pymysql.connect('accountmngsystem.mysql.pythonanywhere-services.com','accountmngsystem','Postgres','accountmngsystem$gbs')
        cursor=connection.cursor()
        cursor.execute("Insert into account (AccountNo,FirstName,LastName,DOB,Address,Email,PhoneNo) values (%s,%s,%s,%s,%s,%s,%s)",(AccountNo,FirstName,LastName,DateOfBirth,Address,Email,ContactNo))
        connection.commit()
        connection.close()
    except Exception as e:
        AccountNo = "Error Creating Account ", e
    return AccountNo

def getAccount(AccountNo):
    try:
        connection =pymysql.connect('accountmngsystem.mysql.pythonanywhere-services.com','accountmngsystem','Postgres','accountmngsystem$gbs')
        cursor=connection.cursor()
        cursor.execute("Select * from account where AccountNo='{}'".format(AccountNo))
        data=cursor.fetchall()[0]
    except Exception as e:
        data = "Error Fetching Account Details",e
    return data

