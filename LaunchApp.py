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
        Address = request.form['lastname']
        AccountDetails = {"FirstName":FirstName,"LastName":LastName,
                          "DateOfBirth":DateOfBirth,"Address":Address}
        AccountNumber = CreateAccount.createAccount(AccountDetails)
        return AccountNumber
    else:
        render_template('registration.html')
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)
