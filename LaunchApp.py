from flask import Flask,render_template,request
import datetime
import CreateAccount
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('registration.html')

@app.route('/createaccount',methods =['POST','GET'])
def createaccount():
    if request.method == 'POST':
        FirstName = request.form['firstname']
        LastName = request.form['lastname']
        DateOfBirth = datetime.datetime.strptime(request.form['dob'], "%Y-%m-%d")
        DateOfBirth = DateOfBirth.strftime("%j%y")
        Address = request.form['address']
        Email = request.form['email']
        ContactNo = request.form['contactno']
        AccountDetails = {"FirstName":FirstName,"LastName":LastName,
                          "DateOfBirth":DateOfBirth,"Address":Address,
                          "Email":Email,"ContactNo":ContactNo}
        AccountNumber = CreateAccount.createAccount(AccountDetails)
        return AccountNumber

    else:
        return render_template('registration.html')

@app.route('/getaccount/<AccountNumber>',methods =['POST','GET'])
def getaccount(AccountNumber):
    AccData = CreateAccount.getAccount(AccountNumber)
    AccountDetails = '<h1> Account Details </h1><br>'
    AccountDetails += '<b>Name:</b><p>{}{}<p><br>'.format(AccData[1],AccData[2])
    AccountDetails += '<b>Account Number:</b><p>{}<p><br>'.format(AccData[0])
    AccountDetails += '<b>Address:</b><p>{}<p><br>'.format(AccData[4])
    AccountDetails += '<b>Email:</b><p>{}<p><br>'.format(AccData[5])
    AccountDetails += '<b>Phone:</b><p>{}<p><br>'.format(AccData[6])
    return AccountDetails
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)