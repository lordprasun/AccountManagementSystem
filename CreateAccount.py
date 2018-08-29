def createAccount(AccountDetails):
    count = 1
    FirstName = AccountDetails["FirstName"]
    LastName = AccountDetails["LastName"]
    Name = (FirstName + LastName).upper()
    DateOfBirth = AccountDetails["DateOfBirth"]
    Address = AccountDetails["Address"]
    AccountNo = Name[:4]+ DateOfBirth + ("{:05d}".format(count))
    return AccountNo