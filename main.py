
## This is just the raw logic understanding and its improved final
## version is updated_main.py
import json
import random
import string
from pathlib import Path

class Bank :
    ##file handling of dummy data file that will get loaded
    #when we run the code and update the data so that we dont
    #need to access the json again and again
   
    database = 'data.json'
    data = [] ## dummy data loaded in main just to work on it
    try :
        if Path(database).exists():
            with open(database) as fs:
                contents = fs.read().strip()
                if contents:
                    try:
                        data = json.loads(contents)
                    except json.JSONDecodeError:
                        records = []
                        for line in contents.splitlines():
                            records.extend(json.loads(line))
                        data = list({record['acc_no']: record for record in records}.values())
        else :
            print("No such account exists !!")
    except Exception as err:
        print(f"an error occured as {err}")



#Updating the dummy file
    @classmethod
    def __update(cls):
        with open(cls.database ,'w') as fs:  ##opening the database file in write mode
            fs.write(json.dumps(Bank.data)) 

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters , k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%" ,k=1)
        id = alpha+spchar+num
        random.shuffle(id)
        return "".join(id)



    # Creating the Account
    def creatingaccount(self):
        info =  {
            "name" : input("Tell your name :- "),
            "age" : int(input("Tell your age :- ")),
            "email": input("Tell your email :- "),
            "pin" : input("Enter your 4 digit pin :- "),
            "acc_no" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if(info['age'] < 18 or len(str(info['pin'])) != 4 ):
            print("account can't be created !!! sorry man ")
        else :
            print("Account has been created succesfully---")
            print("Note down your account details ")
            for i in info :
                print(f"{i} : {info[i]}")
            Bank.data.append(info) ## new info has been appended to the dummy data
            Bank.__update()

    def depositmoney(self):
        accountnum = input("Enter your account number:-")
        enterpin = input("Enter your pin :-")

        userdata = [i for i in Bank.data if i['acc_no'] == accountnum and i['pin'] ==enterpin]
        if not userdata:
            print("No account found")
        else:
            money = int(input("How much you want to deposit :-"))
            if money > 10000 or money <= 0:
                print("You can deposit maximum of 10000 only")
            else:
                print(userdata)
                userdata[0]['balance'] += money
                Bank.__update()
                print(f"Amount of {money} deposited succesfully")

    def withdrawmoney(self):
            accountnum = input("Enter your account number:-")
            enterpin = input("Enter your pin :-")
    
            userdata = [i for i in Bank.data if i['acc_no'] == accountnum and i['pin'] ==enterpin]
            if not userdata:
                print("No account found")
            else:
                money = int(input("How much you want to withdraw :-"))
                if userdata[0]['balance'] < money :
                    print("Sorry you dont have this much amount dude ,,earn it")
                else:
                    print(userdata)
                    userdata[0]['balance'] -= money
                    Bank.__update()
                    print(f"Amount of {money} withdrawn succesfully")
    
    def showdetails(self):
        accountnum = input("Enter your account number:-")
        enterpin = input("Enter your pin :-")
            
        userdata = [i for i in Bank.data if i['acc_no'] == accountnum and i['pin'] ==enterpin]
        print("your information :- \n")
        for i in userdata[0]:
            print(f" {i} : {userdata[0][i]}")



    def updatedetails(self):
        accnumber = input("please tell your account number ")
        pin = input("please tell your pin aswell ")

        userdata = [i for i in Bank.data if i['acc_no'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("no such user found ")
            return

        account = userdata[0]
        print("you cannot change the age, account number, balance")

        print("Fill the details for change or leave it empty if no change")

        newdata = {
            "name": input("please tell new name or press enter : "),
            "email": input("please tell your new Email or press enter to skip :"),
            "pin": input("enter new Pin or press enter to skip: ")
        }

        for field, value in newdata.items():
            if value:
                account[field] = value

        Bank.__update()
        print("details updated successfully")


    def Delete(self):
        accnumber = input("please tell your account number ")
        pin = input("please tell your pin aswell ")

        userdata = [i for i in Bank.data if i['acc_no'] == accnumber and i['pin'] == pin]
              

        if not userdata:
            print("sorry no such data exist ")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()





user = Bank()
print("Press 1 for Creating a account :-")
print("Press 2 for Deposit in the account :-")
print("Press 3 for Withdrawing from account :-")
print("Press 4 for Details of account :-")
print("Press 5 for Updating the details of the account :-")
print("Press 6 for Deleting the account :-")

check = int(input("Enter your response :- "))

if check == 1:
    user.creatingaccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.Delete()